package app.controllers

import org.springframework.web.bind.annotation.*
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity


import app.entities.Product
import app.services.ProductService
import app.services.auth.AuthServiceEager

@RestController
@RequestMapping("/products")
class ProductController(private val productService: ProductService) {

    @Autowired
    private lateinit var authService: AuthServiceEager

    @GetMapping
    fun getAll(): ResponseEntity<Any> {
        val currentUser = authService.getCurrentUser()

        return if (currentUser != null) {
            ResponseEntity(productService.getAll(), HttpStatus.OK)
        } else {
            ResponseEntity(HttpStatus.UNAUTHORIZED)
        }
    }

    @GetMapping("/{id}")
    fun getById(@PathVariable id: Long): ResponseEntity<Any> {
        val currentUser = authService.getCurrentUser()

        return if (currentUser != null) {
            val product = productService.getById(id)
            if (product != null) ResponseEntity(product, HttpStatus.OK)
            else ResponseEntity(HttpStatus.NOT_FOUND)
        } else {
            ResponseEntity(HttpStatus.UNAUTHORIZED)
        }
    }
}