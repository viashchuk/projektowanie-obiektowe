
package app.services.auth

import org.springframework.stereotype.Service

import app.entities.userStorage
import app.entities.User

@Service
class AuthServiceLazy private constructor() {

    companion object {
        val instance: AuthServiceLazy by lazy {
            println("AuthServiceLazy")
            AuthServiceLazy()
        }
    }

    private var currentUser: User? = null

    fun login(name: String, password: String): Boolean {
        println("Test")
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