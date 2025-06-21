package com.example.app.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.app.entities.Order
import androidx.compose.runtime.*
import io.realm.kotlin.Realm

@Composable
fun OrderConfirmation(navController: NavController, realm: Realm, orderId: String) {
    val order = remember(orderId) {
        realm.query(Order::class, "id == $0", orderId).first().find()
    }

    Column(modifier = Modifier
        .fillMaxSize()
        .padding(16.dp)) {
        Text("Thank you for your order!", modifier = Modifier.padding(bottom = 12.dp))

        Spacer(modifier = Modifier.height(24.dp))
        if (order != null) {
            Spacer(modifier = Modifier.height(12.dp))
            Text("Order ID: ${order.id}")
            Text("Status: ${order.status}")
            Text("Total: ${order.totalAmount} zł")
            Spacer(modifier = Modifier.height(16.dp))
            Text("Items:")
            Spacer(modifier = Modifier.height(8.dp))

            order.items.forEach { item ->
                val product = item.product
                Column(modifier = Modifier.padding(bottom = 8.dp)) {
                    Text("${product?.title ?: "Unknown"}")
                    Text("Quantity: ${item.quantity}")
                    Text("Price per item: ${product?.price ?: 0.0} zł")
                }
            }
        } else {
            Text("Order not found")
        }

    }
}