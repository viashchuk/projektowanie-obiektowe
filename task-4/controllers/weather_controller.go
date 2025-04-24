package controllers

import (
	"net/http"

	"github.com/labstack/echo/v4"
	
	"task-4/services"
)

func (c *Controller) GetWeather(ctx echo.Context) error {
	city := ctx.QueryParam("city")
	result, _ := services.GetCityWeather(city)
	return ctx.JSON(http.StatusOK, result)
}