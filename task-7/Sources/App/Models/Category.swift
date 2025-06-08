import Fluent
import Vapor 
import struct Foundation.UUID

final class Category: Model, Content, @unchecked Sendable {
    static let schema = "categories"
    
    @ID(key: .id)
    var id: UUID?

    @Field(key: "title")
    var title: String

    @Children(for: \.$category)
    var products: [Product]

    init() { }

    init(id: UUID? = nil, title: String) {
        self.id = id
        self.title = title
    }
    
    func toDTO() -> CategoryDTO {
        .init(
            id: self.id,
            title: self.title
        )
    }
}
