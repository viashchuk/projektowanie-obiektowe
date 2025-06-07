import NIOSSL
import Fluent
import FluentSQLiteDriver
import Leaf
import Vapor
import Redis

public func configure(_ app: Application) async throws {
    app.databases.use(DatabaseConfigurationFactory.sqlite(.file("db.sqlite")), as: .sqlite)
    app.redis.configuration = try RedisConfiguration(hostname: "localhost")

    app.migrations.add(CreateProduct())
    app.migrations.add(CreateCategory())
    try app.autoMigrate().wait()

    app.views.use(.leaf)

    try routes(app)
}
