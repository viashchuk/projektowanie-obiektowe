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

    init() { }

    init(id: UUID? = nil, title: String, price: Double) {
        self.id = id
        self.title = title
        self.price = price
    }
    
    func toDTO() -> ProductDTO {
        .init(
            id: self.id,
            title: self.$title.value,
            price: self.$price.value
        )
    }
}
