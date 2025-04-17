package app.services

import app.entities.Product
import app.entities.productStorage
import org.springframework.stereotype.Service

@Service
class ProductService {

    fun getAll(): List<Product> = productStorage

    fun getById(id: Long): Product? = productStorage.find { it.id == id }
}