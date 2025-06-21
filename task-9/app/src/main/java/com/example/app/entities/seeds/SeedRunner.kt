package com.example.app.entities.seeds

import io.realm.kotlin.Realm

object SeedRunner {
    fun run(realm: Realm) {
        CategorySeeder.seed(realm)
        ProductSeeder.seed(realm)
    }
}