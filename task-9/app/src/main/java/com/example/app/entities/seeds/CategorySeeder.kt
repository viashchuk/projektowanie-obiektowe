package com.example.app.entities.seeds

import io.realm.kotlin.Realm
import java.util.UUID
import com.example.app.entities.CategoryRealm

object CategorySeeder {
    fun seed(realm: Realm) {
        val categories = listOf(
            CategoryRealm().apply {
                id = UUID.randomUUID().toString()
                title = "Laptopy"
            },
            CategoryRealm().apply {
                id = UUID.randomUUID().toString()
                title = "MacBooki"
            },
            CategoryRealm().apply {
                id = UUID.randomUUID().toString()
                title = "Tablety"
            },
            CategoryRealm().apply {
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