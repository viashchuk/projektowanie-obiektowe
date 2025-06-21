package com.example.app.entities

import io.realm.kotlin.types.RealmObject
import io.realm.kotlin.types.annotations.PrimaryKey

class CategoryRealm : RealmObject {
    @PrimaryKey
    var id: String = ""
    var title: String = ""
}