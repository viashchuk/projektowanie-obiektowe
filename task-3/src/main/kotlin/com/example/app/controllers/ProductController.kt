package app.controllers

import org.springframework.web.bind.annotation.*
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity

import app.entities.Product
import app.services.ProductService

@RestController
@RequestMapping("/products")
class ProductController(private val productService: ProductService) {

    @GetMapping
    fun getAll(): List<Product> = productService.getAll()

    @GetMapping("/{id}")
    fun getById(@PathVariable id: Long): ResponseEntity<Product> {
        val product = productService.getById(id)
        return if (product != null) ResponseEntity(product, HttpStatus.OK)
        else ResponseEntity(HttpStatus.NOT_FOUND)
    }
}