package controllers

import (
	"errors"
	"net/http"

	"github.com/labstack/echo/v4"

	"server/models"
	"server/utils"
)

func (c *Controller) GetOrders(ctx echo.Context) error {
	orders, err := c.repo.GetOrders()
	if err != nil {
		return ctx.JSON(http.StatusInternalServerError, echo.Map{"error": err.Error()})
	}

	if len(orders) == 0 {
		return ctx.NoContent(http.StatusNoContent)
	}

	return ctx.JSON(http.StatusOK, orders)
}

func (c *Controller) CreateOrder(ctx echo.Context) error {
	var order models.Order

	if err := ctx.Bind(&order); err != nil {
		return utils.ErrorResponse(ctx, http.StatusBadRequest, err)
	}

	if len(order.OrderItems) == 0 {
		return utils.ErrorResponse(ctx, http.StatusBadRequest, errors.New("order must contain at least one item"))
	}

	newOrder, err := c.repo.CreateOrder(order)

	if err != nil {
		return utils.ErrorResponse(ctx, http.StatusInternalServerError, err)
	}

	return ctx.JSON(http.StatusCreated, newOrder)
}