import Fluent
import Vapor 
import struct Foundation.UUID

final class Post: Model, Content, @unchecked Sendable {
    static let schema = "posts"
    
    @ID(key: .id)
    var id: UUID?

    @Field(key: "title")
    var title: String

    @Field(key: "body")
    var body: String

    init() { }

    init(id: UUID? = nil, title: String, body: String) {
        self.id = id
        self.title = title
        self.body = body
    }
    
    func toDTO() -> PostDTO {
        .init(
            id: self.id,
            title: self.title,
            body: self.body
        )
    }
}