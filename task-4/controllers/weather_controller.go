package controllers

import (
	// "net/http"

	"github.com/labstack/echo/v4"

	// "task-4/utils"
)

func (c *Controller) GetWeather(ctx echo.Context) error {
	return ctx.String(200, "Your weather is ...")
}