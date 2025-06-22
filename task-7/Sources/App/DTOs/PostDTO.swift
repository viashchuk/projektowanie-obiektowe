import Fluent
import Vapor

struct PostDTO: Content {
    var id: UUID?
    var title: String
    var body: String
    
    func toModel() -> Post {
        let model = Post()
        
        model.id = self.id
        model.title = self.title
        model.body = self.body
        
        return model
    }
}
