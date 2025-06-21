package com.example.app.entities

import java.util.UUID

import io.realm.kotlin.types.annotations.PrimaryKey
import io.realm.kotlin.types.RealmObject

class OrderItem : RealmObject {
    @PrimaryKey
    var id: String = UUID.randomUUID().toString()

    var product: Product? = null
    var quantity: Int = 1
}