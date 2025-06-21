package com.example.app.screens

import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.navigation.NavController
import com.example.app.entities.CartItemStorage
import com.stripe.android.paymentsheet.PaymentSheet

import io.realm.kotlin.Realm

import com.example.app.services.CheckoutService

@Composable
fun CartScreen(realm: Realm, navController: NavController) {
    val context = LocalContext.current
    var orderId by remember { mutableStateOf<String?>(null) }

    val totalAmount = CartItemStorage.sumOf { it.amount * it.product.price }
    val amount = (totalAmount * 100).toInt()

    val paymentSheet = remember {
        PaymentSheet.Builder { result ->
            orderId?.let { CheckoutService.handlePaymentResult(result, navController, realm, it) }
        }
    }.build()

    LaunchedEffect(Unit) {
        CheckoutService.initializeStripe(context, amount) {}
    }

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
            Text("Total: $totalAmount zł")
            Spacer(modifier = Modifier.height(32.dp))

            Button(
                onClick = {
                    CheckoutService.checkout(
                        realm = realm,
                        paymentSheet = paymentSheet,
                        setOrderId = { orderId = it }
                    )
                }
            ) {
                Text("Checkout")
            }
        }
    }
}