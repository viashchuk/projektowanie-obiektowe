package com.example.app.entities

import kotlinx.serialization.Serializable

@Serializable
data class CartItem (
    val id: String,
    val amount: Int,
    val product: Product
)
val CartItemStorage = mutableListOf<CartItem>()