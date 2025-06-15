package com.example.app.entities.seeds

import com.example.app.entities.Category
import com.example.app.entities.categoryStorage

object CategorySeeder {
    fun seed(): Map<String, Category> {
        val categories = listOf(
            Category("laptopy", "Laptopy"),
            Category("mac_booki", "MacBooki"),
            Category("tablety", "Tablety"),
            Category("komputery_gamingowe", "Komputery gamingowe")
        )
        categoryStorage.addAll(categories)

        return categories.associateBy { it.id }
    }
}