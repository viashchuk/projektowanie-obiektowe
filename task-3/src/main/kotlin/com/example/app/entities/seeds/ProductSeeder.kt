package app.entities.seeds

import app.entities.Product
import app.entities.productStorage
import jakarta.annotation.PostConstruct
import org.springframework.stereotype.Component


@Component
class ProductSeed {

    @PostConstruct
    fun loadProducts() {
        val initialProducts = listOf(
            Product(id = 1, title = "MacBook Pro", price = 6999.99, amount = 1),
            Product(id = 2, title = "AirPods Pro", price = 1000.00, amount = 12),
            Product(id = 3, title = "iPhone 16", price = 4000.00, amount = 6)
        )

        productStorage.addAll(initialProducts)
    }
}