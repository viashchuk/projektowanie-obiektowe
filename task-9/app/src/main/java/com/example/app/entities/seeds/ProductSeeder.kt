package com.example.app.entities.seeds

import java.util.UUID
import io.realm.kotlin.Realm
import com.example.app.entities.ProductRealm
import com.example.app.entities.CategoryRealm

object ProductSeeder {
    fun seed(realm: Realm) {
        realm.writeBlocking {
            val laptopsCategory =
                query(CategoryRealm::class, "title == $0", "Laptopy").first().find()
            val macbooksCategory =
                query(CategoryRealm::class, "title == $0", "MacBooki").first().find()
            val tabletsCategory =
                query(CategoryRealm::class, "title == $0", "Tablety").first().find()

            val products = listOf(
                ProductRealm().apply {
                    id = UUID.randomUUID().toString()
                    title = "LENOVO IdeaPad Slim 3 15IRH10 15.3"
                    price = 2699.00
                    amount = 10
                    category = laptopsCategory
                },
                ProductRealm().apply {
                    id = UUID.randomUUID().toString()
                    title = "HP ProBook 450 G10 15.6"
                    price = 2799.00
                    amount = 1
                    category = laptopsCategory
                },
                ProductRealm().apply {
                    id = UUID.randomUUID().toString()
                    title = "ASUS Vivobook A1504VA-BQ940W 15.6"
                    price = 2999.00
                    amount = 2
                    category = laptopsCategory
                },
                ProductRealm().apply {
                    id = UUID.randomUUID().toString()
                    title = "APPLE MacBook Air 13.3"
                    price = 3299.00
                    amount = 1
                    category = macbooksCategory
                },
                ProductRealm().apply {
                    id = UUID.randomUUID().toString()
                    title = "APPLE MacBook Pro 2024 14"
                    price = 9148.00
                    amount = 2
                    category = macbooksCategory
                },
                ProductRealm().apply {
                    id = UUID.randomUUID().toString()
                    title = "Tablet SAMSUNG Galaxy Tab S10 FE 10.9"
                    price = 2399.00
                    amount = 2
                    category = tabletsCategory
                },
                ProductRealm().apply {
                    id = UUID.randomUUID().toString()
                    title = "Tablet APPLE iPad Air 11"
                    price = 2999.00
                    amount = 2
                    category = tabletsCategory
                }
            )

            products.forEach { product ->
                copyToRealm(product)
            }
        }
    }
}