import Fluent
import Vapor

struct CategoryController: RouteCollection {
    func boot(routes: any RoutesBuilder) throws {
        let categories = routes.grouped("categories")

        categories.get(use: index)
        categories.get("new", use: new)
        categories.post(use: create)

        categories.group(":id") { category in
            category.get(use: show)
            category.get("edit", use: edit)
            category.post("update", use: update)
            category.post("delete", use: delete)
        }
    }

    struct CategoryListContext: Encodable {
    let categories: [Category]
}

    @Sendable
    func index(req: Request) throws -> EventLoopFuture<View> {
        return Category.query(on: req.db).all().flatMap { categories in
            let context = ["categories": categories]
            return req.view.render("categories/index", context)
        }
    }

    func new(req: Request) throws -> EventLoopFuture<View> {
        return req.view.render("categories/new")
    }

    func create(req: Request) async throws -> Response {
        let category = try req.content.decode(CategoryDTO.self).toModel()
        try await category.save(on: req.db)

        return req.redirect(to: "/categories")
    }
    
    @Sendable
    func show(req: Request) throws -> EventLoopFuture<View> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Category.find(id, on: req.db).flatMap { category in
            guard let category = category else {
                return req.eventLoop.future(error: Abort(.notFound))
            }

            let context = ["category": category]
            return req.view.render("categories/show", context)
        }
    }

    @Sendable
    func edit(req: Request) throws -> EventLoopFuture<View> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Category.find(id, on: req.db).flatMap { category in
            guard let category = category else {
                return req.eventLoop.future(error: Abort(.notFound))
            }

            let context = ["category": category]
            return req.view.render("categories/edit", context)
        }
    }

    func update(req: Request) async throws -> Response {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        guard let category = try await Category.find(id, on: req.db) else {
            throw Abort(.notFound)
        }
        
        let categoryDto = try req.content.decode(CategoryDTO.self)
        category.title = categoryDto.title

        try await category.update(on: req.db)

        return req.redirect(to: "/categories/\(id)")
    }

    @Sendable
    func delete(req: Request) async throws -> Response {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        guard let category = try await Category.find(id, on: req.db) else {
            throw Abort(.notFound)
        }

        try await category.delete(on: req.db)
        return req.redirect(to: "/categories")
    }
}