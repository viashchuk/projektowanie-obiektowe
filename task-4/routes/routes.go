package routes

import (
	"task-4/controllers"

	"github.com/labstack/echo/v4"
)

func SetupRoutes(e *echo.Echo, c *controllers.Controller) {
	e.GET("/weather", c.GetWeather)
}
