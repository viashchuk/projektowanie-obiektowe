import Fluent

struct CreateProduct: AsyncMigration {
    func prepare(on database: any Database) async throws {
        try await database.schema("products")
            .id()
            .field("title", .string, .required)
            .field("price", .double, .required)
            .create()
    }

    func revert(on database: any Database) async throws {
        try await database.schema("products").delete()
    }
}
