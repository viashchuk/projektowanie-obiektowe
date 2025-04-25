package controllers

import (
	"net/http"
	"strings"

	"github.com/labstack/echo/v4"

	"task-4/services"
)

type WeatherRequest struct {
	Cities string `query:"cities"`
}

func (c *Controller) GetWeather(ctx echo.Context) error {
	var req WeatherRequest
	
	if err := ctx.Bind(&req); err != nil {
		return ctx.JSON(http.StatusBadRequest, map[string]string{"error": "Invalid request parameters"})
	}
	if req.Cities == "" {
		return ctx.JSON(http.StatusBadRequest, map[string]string{"error": "Parameter 'cities' is required"})
	}

	cities := strings.Split(req.Cities, ",")

	var results []services.WeatherSummary

	for _, city := range cities {
		city_weather, err := services.GetCityWeather(city, c.repo)
		if err != nil {
			continue
		}
		results = append(results, *city_weather)
	}

	return ctx.JSON(http.StatusOK, results)
}