package com.example.app.services

import java.util.UUID

import com.example.app.entities.ProductRealm
import com.example.app.entities.CartItemStorage
import com.example.app.entities.CartItem

fun addToCart(product: ProductRealm) {
    val existingItem = CartItemStorage.find { it.product.id == product.id }

    if (existingItem != null) {
        val updatedItem = existingItem.copy(amount = existingItem.amount + 1)
        CartItemStorage.remove(existingItem)
        CartItemStorage.add(updatedItem)
    } else {
        CartItemStorage.add(
            CartItem(
                id = UUID.randomUUID().toString(),
                amount = 1,
                product = product
            )
        )
    }
}