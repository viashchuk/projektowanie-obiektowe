package com.example.app.entities.seeds

import io.realm.kotlin.Realm
import java.util.UUID
import com.example.app.entities.Category

object CategorySeeder {
    fun seed(realm: Realm) {
        val categories = listOf(
            Category().apply {
                id = UUID.randomUUID().toString()
                title = "Laptopy"
            },
            Category().apply {
                id = UUID.randomUUID().toString()
                title = "MacBooki"
            },
            Category().apply {
                id = UUID.randomUUID().toString()
                title = "Tablety"
            },
            Category().apply {
                id = UUID.randomUUID().toString()
                title = "Komputery Gamingowe"
            }
        )

        realm.writeBlocking {
            categories.forEach { category ->
                copyToRealm(category)
            }
        }
    }
}