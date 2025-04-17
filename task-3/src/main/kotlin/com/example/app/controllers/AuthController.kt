package app.controllers

import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import org.springframework.beans.factory.annotation.Autowired

import app.dto.AuthRequest
import app.services.auth.AuthServiceEager

@RestController
class AuthController() {

    @Autowired
    private lateinit var authService: AuthServiceEager

    @PostMapping("/")
    fun login(@RequestBody request: AuthRequest): ResponseEntity<String> {
        return if (authService.login(request.name, request.password)) {
            ResponseEntity("Login ${authService.getCurrentUser()?.name}", HttpStatus.OK)
        } else {
            ResponseEntity(HttpStatus.UNAUTHORIZED)
        }
    }

    @PostMapping("/logout")
    fun logout(): ResponseEntity<String> {
        val currentUser = authService.getCurrentUser()
        return if (currentUser != null) {
            authService.logout()
            ResponseEntity("Logged out ${currentUser.name}", HttpStatus.OK)
        } else {
            ResponseEntity(HttpStatus.BAD_REQUEST)
        }
    }
}