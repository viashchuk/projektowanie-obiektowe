import Fluent
import Vapor

struct CategoryDTO: Content {
    var id: UUID?
    var title: String
    
    func toModel() -> Category {
        let model = Category()
        
        model.id = self.id
        model.title = self.title
        
        return model
    }
}
