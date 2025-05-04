package main

import (
	"server/controllers"
	"server/db"
	"server/repositories"
	"server/routes"
	"server/seeds"

	"github.com/labstack/echo/v4"
    "github.com/labstack/echo/v4/middleware"
)

func main() {

	db := db.InitDB()

	s := seeds.Seed{DB: db}
	s.SeedProducts()

	e := echo.New()
	e.Use(middleware.CORSWithConfig(middleware.CORSConfig{
        AllowOrigins: []string{"http://localhost:5173"},
        AllowMethods: []string{echo.GET, echo.POST},
    }))

	e.Static("/uploads", "uploads")

	repo := &repositories.Repository{DB: db}
	c := controllers.NewController(repo)

	routes.SetupRoutes(e, c)

	e.Logger.Fatal(e.Start(":1323"))
}
