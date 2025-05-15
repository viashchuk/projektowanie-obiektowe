package controllers

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func (c *Controller) GetProducts(ctx echo.Context) error {
	products, err := c.repo.GetProducts()
	if err != nil {
		return ctx.JSON(http.StatusNotFound, echo.Map{"error": err.Error()})
	}

	if len(products) == 0 {
		return ctx.NoContent(http.StatusNoContent)
	}

	return ctx.JSON(http.StatusOK, products)
}