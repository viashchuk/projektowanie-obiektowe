package app.entities

data class Product(
    val id: Long,
    val title: String,
    val price: Double,
    val amount: Int
)

val productStorage = mutableListOf<Product>()