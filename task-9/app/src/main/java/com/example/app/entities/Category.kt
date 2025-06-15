package com.example.app.entities

import kotlinx.serialization.Serializable

@Serializable
data class Category (
    val id: String,
    val title: String
)
val categoryStorage = mutableListOf<Category>()