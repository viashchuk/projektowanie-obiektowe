package com.example.app.services

import android.content.Context
import androidx.navigation.NavController
import com.example.app.entities.*
import com.github.kittinunf.fuel.httpPost
import com.github.kittinunf.fuel.json.responseJson
import com.github.kittinunf.result.Result
import com.stripe.android.PaymentConfiguration
import com.stripe.android.paymentsheet.PaymentSheet
import com.stripe.android.paymentsheet.PaymentSheetResult
import io.realm.kotlin.Realm
import io.realm.kotlin.ext.toRealmList
import org.json.JSONObject
import java.util.*

object CheckoutService {

    var customerConfig: PaymentSheet.CustomerConfiguration? = null
    var paymentIntentClientSecret: String? = null

    fun initializeStripe(context: Context, amount: Int, onReady: () -> Unit) {
        val jsonBody = JSONObject().put("amount", amount).toString()

        "http://10.0.2.2:3000/payment-sheet"
            .httpPost()
            .header("Content-Type" to "application/json")
            .body(jsonBody)
            .responseJson { _, _, result ->
                if (result is Result.Success) {
                    val responseJson = result.get().obj()
                    paymentIntentClientSecret = responseJson.getString("paymentIntent")
                    customerConfig = PaymentSheet.CustomerConfiguration(
                        id = responseJson.getString("customer"),
                        ephemeralKeySecret = responseJson.getString("ephemeralKey")
                    )
                    val publishableKey = responseJson.getString("publishableKey")
                    PaymentConfiguration.init(context, publishableKey)
                    onReady()
                } else {
                    println(result)
                }
            }
    }

    fun createOrder(realm: Realm): Order {
        return realm.writeBlocking {
            val orderItems = CartItemStorage.map { cartItem ->
                OrderItem().apply {
                    product = query(Product::class, "id == $0", cartItem.product.id).first().find()
                    quantity = cartItem.amount
                }
            }.toRealmList()

            val order = Order().apply {
                id = UUID.randomUUID().toString()
                totalAmount = CartItemStorage.sumOf { it.amount * it.product.price }
                status = OrderStatus.PENDING.name
                items = orderItems
            }

            copyToRealm(order)
        }
    }

    fun handlePaymentResult(
        result: PaymentSheetResult,
        navController: NavController,
        realm: Realm,
        orderId: String
    ) {
        realm.writeBlocking {
            val order = query(Order::class, "id == $0", orderId).first().find()
            if (order != null) {
                order.status = when (result) {
                    is PaymentSheetResult.Completed -> OrderStatus.PAID.name
                    is PaymentSheetResult.Canceled, is PaymentSheetResult.Failed -> OrderStatus.FAILED.name
                }
            }
        }

        if (result is PaymentSheetResult.Completed) {
            CartItemStorage.clear()
            navController.navigate("order_confirmation/$orderId")
        }
    }

    fun checkout(
        realm: Realm,
        paymentSheet: PaymentSheet,
        setOrderId: (String) -> Unit
    ) {
        val config = customerConfig
        val secret = paymentIntentClientSecret

        if (config != null && secret != null) {
            val createdOrder = createOrder(realm)
            setOrderId(createdOrder.id)

            paymentSheet.presentWithPaymentIntent(
                secret,
                PaymentSheet.Configuration.Builder("My merchant name")
                    .customer(config)
                    .allowsDelayedPaymentMethods(true)
                    .build()
            )
        }
    }
}