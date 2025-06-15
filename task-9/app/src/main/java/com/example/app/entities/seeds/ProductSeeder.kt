package com.example.app.entities.seeds

import com.example.app.entities.Product
import com.example.app.entities.productStorage
import com.example.app.entities.Category

object ProductSeeder {
    fun seed(categoryById: Map<String, Category>) {
        productStorage.addAll(
            listOf(
                Product("LENOVO IdeaPad Slim 3 15IRH10 15.3", 2699.00, 10, categoryById["laptopy"]!!),
                Product("HP ProBook 450 G10 15.6", 2799.00, 1, categoryById["laptopy"]!!),
                Product("ASUS Vivobook A1504VA-BQ940W 15.6", 2999.00, 2, categoryById["laptopy"]!!),

                Product("APPLE MacBook Air 13.3", 3299.00, 1, categoryById["mac_booki"]!!),
                Product("APPLE MacBook Pro 2024 14", 9148.00, 2, categoryById["mac_booki"]!!),

                Product("Tablet SAMSUNG Galaxy Tab S10 FE 10.9", 2399.00, 2, categoryById["tablety"]!!),
                Product("Tablet APPLE iPad Air 11", 2999.00, 2, categoryById["tablety"]!!),

                Product("MAD DOG ENDORFY300ARGB-A07WR16 R5-5600 16GB", 4249.00, 2, categoryById["komputery_gamingowe"]!!),
                Product("MAD DOG GeForce RTX4060 PurePC Edition 2", 4199.00, 2, categoryById["komputery_gamingowe"]!!)
            )
        )
    }
}