package com.example.app.screens

import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

import com.example.app.entities.CartItemStorage
import io.realm.kotlin.Realm

@Composable
fun CartScreen(realm: Realm) {
    Column(modifier = Modifier.padding(16.dp)) {
        if (CartItemStorage.isEmpty()) {
            Text("Cart is empty")
        } else {
            Text("Your Cart", modifier = Modifier.padding(bottom = 8.dp))

            CartItemStorage.forEach { item ->
                Column(modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp)) {
                    Text(item.product.title)
                    Text("Amount: ${item.amount}")
                    Text("Price per item: ${item.product.price} zł")
                    Text("Total: ${item.amount * item.product.price} zł")
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            val total = CartItemStorage.sumOf { it.amount * it.product.price }
            Text("Total: $total zł")
        }
    }
}