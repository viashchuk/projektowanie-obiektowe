import Fluent
import Vapor

struct ProductController: RouteCollection {
    func boot(routes: any RoutesBuilder) throws {
        let products = routes.grouped("products")

        products.get(use: index)
        products.post(use: create)

        products.group(":id") { product in
            product.get(use: show)
            product.put(use: update)
            product.delete(use: delete)
        }
    }

    @Sendable
    func index(req: Request) async throws -> [Product] {
        try await Product.query(on: req.db).all()
    }

    @Sendable
    func create(req: Request) async throws -> Product {
        let product = try req.content.decode(Product.self)
        try await product.save(on: req.db)
        return product
    }

    @Sendable
    func show(req: Request) async throws -> Product {
        guard let product = try await Product.find(req.parameters.get("id"), on: req.db) else {
            throw Abort(.notFound)
        }
        return product
    }

    @Sendable
    func update(req: Request) async throws -> Product {
        guard let product = try await Product.find(req.parameters.get("id"), on: req.db) else {
            throw Abort(.notFound)
        }
        let updatedProduct = try req.content.decode(Product.self)
        product.title = updatedProduct.title
        try await product.save(on: req.db)
        return product
    }

    @Sendable
    func delete(req: Request) async throws -> HTTPStatus {
        guard let product = try await Product.find(req.parameters.get("id"), on: req.db) else {
            throw Abort(.notFound)
        }
        try await product.delete(on: req.db)
        return .ok
    }
}