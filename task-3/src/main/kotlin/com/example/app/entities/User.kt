package app.entities

data class User(
    val id: Long,
    val name: String,
    val password: String
)

val userStorage = mutableListOf<User>()