package com.example.app.screens

import androidx.compose.material3.Text
import androidx.compose.material3.Scaffold
import androidx.compose.material3.ButtonDefaults
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding

import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Button
import androidx.compose.ui.graphics.Color
import androidx.compose.foundation.shape.RoundedCornerShape

import io.realm.kotlin.Realm

import com.example.app.entities.Product
import com.example.app.services.addToCart

@Composable
fun ProductsScreen(realm: Realm) {
    val products = realm.query(clazz = Product::class).find()

    Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
        Row(modifier = Modifier.padding(innerPadding)) {
            ProductsList(products)
        }
    }
}

@Composable
fun ProductsList(products: List<Product>, modifier: Modifier = Modifier) {
    LazyColumn(modifier = modifier) {
        item {
            Text("Products")
        }
        items(products) { product ->
            ProductRow(product)
        }
    }
}

@Composable
fun ProductRow(product: Product) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(8.dp),
        shape = RoundedCornerShape(12.dp),
        colors = CardDefaults.cardColors(containerColor = Color(0xFFd1d5dc)),
        elevation = CardDefaults.cardElevation(4.dp)
    ) {
        Column(modifier = Modifier.padding(12.dp)) {
            Text(text = "Title: ${product.title}")
            Text(text = "Price: ${product.price} zł")
            Text(text = "Amount: ${product.amount}")
            Text(text = "Category: ${product.category?.title ?: "Any"}")

            Spacer(modifier = Modifier.padding(top = 8.dp))

            Button(
                onClick = { addToCart(product) },
                colors = ButtonDefaults.buttonColors(
                    containerColor = Color(0xFF1447e6),
                    contentColor = Color.White
                )
            ) {
                Text("Add to Cart")
            }
        }
    }
}