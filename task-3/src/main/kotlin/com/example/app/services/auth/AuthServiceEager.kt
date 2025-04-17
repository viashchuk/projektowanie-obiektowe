
package app.services.auth

import org.springframework.stereotype.Service

import app.entities.userStorage
import app.entities.User

@Service
object AuthServiceEager {

    private var currentUser: User? = null

    init {
        println("AuthServiceEager")
    }

    fun login(name: String, password: String): Boolean {
        val user = userStorage.find { it.name == name && it.password == password }
        if (user == null) {
            return false
        }
        currentUser = user
        return true
    }

    fun isLoggedIn(userId: Long): Boolean {
        return currentUser?.id == userId
    }

    fun logout() {
        currentUser = null
    }

    fun getCurrentUser(): User? = currentUser
}