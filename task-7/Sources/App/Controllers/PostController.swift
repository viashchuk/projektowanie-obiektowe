import Fluent
import Vapor

struct PostController: RouteCollection {
    func boot(routes: any RoutesBuilder) throws {
        let posts = routes.grouped("posts")

        posts.get(use: index)
        posts.get("new", use: new)
        posts.post(use: create)

        posts.group(":id") { post in
            post.get(use: show)
            post.get("edit", use: edit)
            post.post("update", use: update)
            post.post("delete", use: delete)
        }
    }

    struct PostListContext: Encodable {
    let posts: [Post]
}

    @Sendable
    func index(req: Request) throws -> EventLoopFuture<View> {
        return Post.query(on: req.db).all().flatMap { posts in
            let context = ["posts": posts]
            return req.view.render("posts/index", context)
        }
    }

    func new(req: Request) throws -> EventLoopFuture<View> {
        return req.view.render("posts/new")
    }

    func create(req: Request) async throws -> Response {
        let post = try req.content.decode(PostDTO.self).toModel()
        try await post.save(on: req.db)

        return req.redirect(to: "/posts")
    }
    
    @Sendable
    func show(req: Request) throws -> EventLoopFuture<View> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Post.find(id, on: req.db).flatMap { post in
            guard let post = post else {
                return req.eventLoop.future(error: Abort(.notFound))
            }

            let context = ["post": post]
            return req.view.render("posts/show", context)
        }
    }

    @Sendable
    func edit(req: Request) throws -> EventLoopFuture<View> {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }

        return Post.find(id, on: req.db).flatMap { post in
            guard let post = post else {
                return req.eventLoop.future(error: Abort(.notFound))
            }

            let context = ["post": post]
            return req.view.render("posts/edit", context)
        }
    }

    func update(req: Request) async throws -> Response {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        guard let post = try await Post.find(id, on: req.db) else {
            throw Abort(.notFound)
        }
        
        let postDto = try req.content.decode(PostDTO.self)
        post.title = postDto.title
        post.body = postDto.body

        try await post.update(on: req.db)

        return req.redirect(to: "/posts/\(id)")
    }

    @Sendable
    func delete(req: Request) async throws -> Response {
        guard let id = req.parameters.get("id", as: UUID.self) else {
            throw Abort(.badRequest)
        }
        guard let post = try await Post.find(id, on: req.db) else {
            throw Abort(.notFound)
        }

        try await post.delete(on: req.db)
        return req.redirect(to: "/posts")
    }
}