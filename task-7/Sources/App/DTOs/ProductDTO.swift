import Fluent
import Vapor

struct ProductDTO: Content {
    var id: UUID?
    var title: String
    var price: Double
    var category_id: UUID

    func toModel() -> Product {
        let model = Product()

        model.id = self.id
        model.title = self.title
        model.price = self.price
        model.$category.id = self.category_id

        return model
    }
}