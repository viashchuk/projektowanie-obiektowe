import Fluent
import Vapor
import Redis

struct ProductEditContext: Encodable {
    let product: Product
    let categories: [Category]
}

struct ProductCacheDTO: Codable {
    let id: UUID
    let title: String
    let price: Double
    let categoryTitle: String
}

struct ProductController: RouteCollection {
    func boot(routes: any RoutesBuilder) throws {
        let products = routes.grouped("products")

        products.get(use: index)
        products.get("new", use: new)
        products.post(use: create)

        products.group(":id") { product in
            product.get(use: show)
            product.get("edit", use: edit)
            product.post("update", use: update)
            product.post("delete", use: delete)
        }
    }

    @Sendable
    func index(req: Request) throws -> EventLoopFuture<View> {
        return Product.query(on: req.db).with(\.$category).all().flatMap { products in
            let context = ["products": products]
            return req.view.render("products/index", context)
        }
    }

    func new(req: Request) throws -> EventLoopFuture<View> {
        return Category.query(on: req.db).all().flatMap { categories in
            let context = ["categories": categories]
            return req.view.render("products/new", context)
        }
    }

    func create(req: Request) async throws -> Response {
        let product = try req.content.decode(ProductDTO.self).toModel()
        try await product.save(on: req.db)

        return req.redirect(to: "/products")
    }

    @Sendable
    func show(req: Request) throws -> EventLoopFuture<View> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        let cacheKey = RedisKey("product:\(id)")

        return req.redis.get(cacheKey, asJSON: ProductCacheDTO.self).flatMap { cached in

            if let cached = cached {
                let context: [String: ProductCacheDTO] = ["product": cached]
                return req.view.render("products/show", context)
            }

            return Product.query(on: req.db)
                .with(\.$category)
                .filter(\.$id == id)
                .first()
                .flatMap { product in
                    guard let product = product else {
                        return req.eventLoop.future(error: Abort(.notFound))
                    }

                    let cacheDTO = ProductCacheDTO(
                        id: product.id!,
                        title: product.title,
                        price: product.price,
                        categoryTitle: product.category.title
                    )

                    req.redis.set(cacheKey, toJSON: cacheDTO).whenComplete { result in
                        switch result {
                        case .success:
                            expireTheKey(cacheKey, redis: req.redis)
                        case .failure(let error):
                            print("\(error)")
                        }
                    }

                    let context = ["product": product]
                    return req.view.render("products/show", context)
                }
        }
    }

    @Sendable
    func edit(req: Request) throws -> EventLoopFuture<View> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        
        let categories = Category.query(on: req.db).all()
        let product = Product.query(on: req.db).with(\.$category).filter(\.$id == id).first()

        return product.and(categories).flatMap { product, categories in
            guard let product = product else {
                return req.eventLoop.future(error: Abort(.notFound))
            }

            let context = ProductEditContext(product: product, categories: categories)
            return req.view.render("products/edit", context)
        }
    }

    func update(req: Request) async throws -> Response {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        guard let product = try await Product.find(id, on: req.db) else {
            throw Abort(.notFound)
        }
        
        let productDto = try req.content.decode(ProductDTO.self)
        product.title = productDto.title
        product.price = productDto.price
        product.$category.id = productDto.category_id

        try await product.update(on: req.db)

        return req.redirect(to: "/products/\(id)")
    }

    @Sendable
    func delete(req: Request) async throws -> Response {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        guard let product = try await Product.find(id, on: req.db) else {
            throw Abort(.notFound)
        }

        try await product.delete(on: req.db)
        return req.redirect(to: "/products")
    }
}