import Fluent
import Vapor

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
        return Product.query(on: req.db).all().flatMap { products in
            let context = ["products": products]
            return req.view.render("products/index", context)
        }
    }

    func new(req: Request) throws -> EventLoopFuture<View> {
        return req.view.render("products/new")
    }

    func create(req: Request) throws -> EventLoopFuture<Response> {
        let product = try req.content.decode(Product.self)
        
        return product.save(on: req.db).map {
            req.redirect(to: "/products")
        }
    }
    
    @Sendable
    func show(req: Request) throws -> EventLoopFuture<View> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Product.find(id, on: req.db).flatMap { product in
            guard let product = product else {
                return req.eventLoop.future(error: Abort(.notFound))
            }

            let context = ["product": product]
            return req.view.render("products/show", context)
        }
    }

    @Sendable
    func edit(req: Request) throws -> EventLoopFuture<View> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Product.find(id, on: req.db).flatMap { product in
            guard let product = product else {
                return req.eventLoop.future(error: Abort(.notFound))
            }

            let context = ["product": product]
            return req.view.render("products/edit", context)
        }
    }

    func update(req: Request) throws -> EventLoopFuture<Response> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Product.find(id, on: req.db).flatMap { product in
            guard let product = product else {
                return req.eventLoop.future(error: Abort(.notFound))
            }

            do {
                let updatedProduct = try req.content.decode(Product.self)
                product.title = updatedProduct.title
                product.price = updatedProduct.price

                return product.save(on: req.db).map {
                    req.redirect(to: "/products/\(id)")
                }
            } catch {
                return req.eventLoop.future(error: error)
            }
        }
    }

    @Sendable
    func delete(req: Request) throws -> EventLoopFuture<Response> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Product.find(id, on: req.db).flatMap { product in
            guard let product = product else {
                return req.eventLoop.future(error: Abort(.notFound))
            }

            return product.delete(on: req.db).map {
                req.redirect(to: "/products")
            }
        }
    }
}