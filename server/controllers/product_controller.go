package controllers

import (
	"net/http"

	"github.com/labstack/echo/v4"

	"server/utils"
)

func (c *Controller) GetProducts(ctx echo.Context) error {
	products, err := c.repo.GetProducts()
	if err != nil {
		return ctx.JSON(http.StatusNotFound, echo.Map{"error": err.Error()})
	}

	return ctx.JSON(http.StatusOK, products)
}

func (c *Controller) GetProduct(ctx echo.Context) error {
	id, _ := utils.ParseID(ctx)
	product, err := c.repo.GetProductByID(id)

	if err != nil {
		return utils.ErrorResponse(ctx, http.StatusBadRequest, err)
	}

	return ctx.JSON(http.StatusOK, product)
}