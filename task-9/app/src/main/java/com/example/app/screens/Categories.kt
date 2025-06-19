package com.example.app.screens

import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.layout.padding

import com.example.app.entities.Category
import com.example.app.entities.categoryStorage

@Composable
fun CategoriesScreen() {
    Row(modifier = Modifier.padding(8.dp)) {
        CategoryList(
            categories = categoryStorage,
            modifier = Modifier.weight(1f)
        )
    }
}

@Composable
fun CategoryList(categories: List<Category>, modifier: Modifier = Modifier) {
    LazyColumn(modifier = modifier) {
        item {
            Text("Categories")
        }
        items(categories) { category ->
            Text(text = "Title: ${category.title}", modifier = Modifier.padding(8.dp))
        }
    }
}