package main

import (
	"task-4/controllers"
	"task-4/routes"

	"github.com/labstack/echo/v4"
)

func main() {

	e := echo.New()

	c := controllers.NewController()

	routes.SetupRoutes(e, c)

	e.Logger.Fatal(e.Start(":1323"))
}
