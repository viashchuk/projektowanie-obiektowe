package com.example.app


import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.app.entities.Category
import com.example.app.entities.Product
import com.example.app.entities.categoryStorage
import com.example.app.entities.productStorage
import com.example.app.entities.seeds.SeedRunner
import com.example.app.ui.theme.AppTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        SeedRunner.run()
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            AppTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    Row (modifier = Modifier.padding(innerPadding)) {
                        ProductsList(productStorage)
                        CategoryList(categoryStorage)
                    }
                }
            }
        }
    }
}

@Composable
fun ProductsList(products: List<Product>) {
    Column {
        Text("Products")

        products.forEach { product ->
            ProductRow(product)
        }
    }
}

@Composable
fun ProductRow(product: Product) {
    Row(modifier = Modifier.padding(8.dp)) {
        Column {
            Text(text = "Title: ${product.title}")
            Text(text = "Price: ${product.price} zł")
            Text(text = "Amount: ${product.amount}")
            Text(text = "Category: ${product.category.title}")
        }
    }
}

@Composable
fun CategoryList(categories: List<Category>) {
    Row(modifier = Modifier.padding(8.dp)) {
        Column {
            Text("Categories")

            categories.forEach { category ->
                Column {
                    Text(text = "Title: ${category.title}")
                }
            }
        }
    }
}