package com.example.app.entities

import kotlinx.serialization.Serializable

@Serializable
data class Product (
    val id: String,
    val title: String,
    val price: Double,
    val amount: Int,
    val category: Category
)

val productStorage = mutableListOf<Product>()