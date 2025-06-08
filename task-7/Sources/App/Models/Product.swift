import Fluent
import Vapor 
import struct Foundation.UUID

final class Product: Model, Content, @unchecked Sendable {
    static let schema = "products"
    
    @ID(key: .id)
    var id: UUID?

    @Field(key: "title")
    var title: String

    @Field(key: "price")
    var price: Double

    @Parent(key: "category_id")
    var category: Category

    init() { }

    init(id: UUID? = nil, title: String, price: Double, categoryID: UUID) {
        self.id = id
        self.title = title
        self.price = price
        self.$category.id = categoryID
    }
    
    func toDTO() -> ProductDTO {
        .init(
            id: self.id,
            title: self.title,
            price: self.price,
            category_id: self.$category.id
        )
    }
}
