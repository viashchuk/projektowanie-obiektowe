package com.example.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController

import io.realm.kotlin.Realm
import io.realm.kotlin.RealmConfiguration

import com.example.app.screens.ProductsScreen
import com.example.app.screens.CategoriesScreen
import com.example.app.screens.CartScreen

import com.example.app.entities.Product
import com.example.app.entities.Category
import com.example.app.entities.OrderItem
import com.example.app.entities.Order
import com.example.app.entities.seeds.SeedRunner
import com.example.app.screens.OrderConfirmation

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        val config = RealmConfiguration.create(
            schema = setOf(
                Product::class,
                Category::class,
                Order::class,
                OrderItem::class
            ))
        val realm: Realm = Realm.open(config)

        realm.writeBlocking {
            deleteAll()
        }

        SeedRunner.run(realm)

        super.onCreate(savedInstanceState)
        setContent {
            Main(realm)
        }
    }
}

@Composable
fun Main(realm: Realm) {
    val navController = rememberNavController()
    Column(Modifier.padding(8.dp)) {
        NavBar(navController = navController)
        NavHost(navController, startDestination = NavRoutes.Products.route) {
            composable(NavRoutes.Products.route) { ProductsScreen(realm) }
            composable(NavRoutes.Categories.route) { CategoriesScreen(realm)  }
            composable(NavRoutes.Cart.route) { CartScreen(realm, navController) }
            composable("order_confirmation/{orderId}") { backStackEntry ->
                val orderId = backStackEntry.arguments?.getString("orderId") ?: ""
                OrderConfirmation(navController, realm, orderId)
            }
        }
    }
}
@Composable
fun NavBar(navController: NavController){
    Row(
        Modifier.fillMaxWidth().padding(bottom = 8.dp)){
        Text("Products",
            Modifier
                .weight(0.33f)
                .clickable { navController.navigate(NavRoutes.Products.route) }, fontSize = 22.sp, color= Color(0xFF6650a4))
        Text("Categories",
            Modifier
                .weight(0.33f)
                .clickable { navController.navigate(NavRoutes.Categories.route) }, fontSize = 22.sp, color= Color(0xFF6650a4))
        Text("Cart",
            Modifier
                .weight(0.33f)
                .clickable { navController.navigate(NavRoutes.Cart.route) }, fontSize = 22.sp, color= Color(0xFF6650a4))
    }
}

sealed class NavRoutes(val route: String) {
    object Products : NavRoutes("products")
    object Categories : NavRoutes("categories")
    object Cart : NavRoutes("cart")
    object OrderConfirmation : NavRoutes("order-confirmation")
}