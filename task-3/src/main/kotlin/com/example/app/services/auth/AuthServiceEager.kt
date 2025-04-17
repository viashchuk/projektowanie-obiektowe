
package app.services.auth

import org.springframework.stereotype.Service

import app.entities.userStorage

@Service
object AuthServiceEager {
    init {
        println("AuthServiceEager")
    }

    fun isLoggedIn(userId: Long): Boolean {
        return userStorage.any { it.id == userId }
    }
}