package com.example.app.entities

import io.realm.kotlin.types.annotations.PrimaryKey
import io.realm.kotlin.types.RealmObject

class ProductRealm : RealmObject {
    @PrimaryKey
    var id: String = ""
    var title: String = ""
    var price: Double = 0.0
    var amount: Int = 0
    var category: CategoryRealm? = null
}