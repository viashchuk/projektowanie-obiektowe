package com.example.app.entities

import java.util.UUID

import io.realm.kotlin.types.annotations.PrimaryKey
import io.realm.kotlin.types.RealmObject
import io.realm.kotlin.types.RealmList
import io.realm.kotlin.ext.realmListOf

class Order : RealmObject {
    @PrimaryKey
    var id: String = UUID.randomUUID().toString()

    var items: RealmList<OrderItem> = realmListOf()
    var totalAmount: Double = 0.0
    var status: String = OrderStatus.PENDING.name
    var createdAt: Long = System.currentTimeMillis()
}