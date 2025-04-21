package routes

import (
	"server/controllers"

	"github.com/labstack/echo/v4"
)

func SetupRoutes(e *echo.Echo, c *controllers.Controller) {
	e.GET("/products", c.GetProducts)
	e.GET("/products/:id", c.GetProduct)

	e.GET("/orders", c.GetOrders)
	e.GET("/orders/:id", c.GetOrder)
	e.POST("/orders", c.CreateOrder)
}
