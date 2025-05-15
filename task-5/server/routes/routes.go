package routes

import (
	"server/controllers"

	"github.com/labstack/echo/v4"
)

func SetupRoutes(e *echo.Echo, c *controllers.Controller) {
	e.GET("/products", c.GetProducts)

	e.GET("/orders", c.GetOrders)
	e.POST("/orders", c.CreateOrder)
}
