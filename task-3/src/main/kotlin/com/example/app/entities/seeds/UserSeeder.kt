package app.entities.seeds

import app.entities.User
import app.entities.userStorage
import jakarta.annotation.PostConstruct
import org.springframework.stereotype.Component


@Component
class UserSeed {

    @PostConstruct
    fun loadProducts() {
        val users = listOf(
            User(id = 1, name = "user1", password = "userpassword"),
            User(id = 1, name = "admin", password = "adminpassword")
        )

        userStorage.addAll(users)
    }
}