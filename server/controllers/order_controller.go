package controllers

import (
	"net/http"

	"github.com/labstack/echo/v4"

	"server/models"
	"server/utils"
)

func (c *Controller) GetOrders(ctx echo.Context) error {
	orders, err := c.repo.GetOrders()
	if err != nil {
		return ctx.JSON(http.StatusNotFound, echo.Map{"error": err.Error()})
	}

	return ctx.JSON(http.StatusOK, orders)
}

func (c *Controller) GetOrder(ctx echo.Context) error {
	id, _ := utils.ParseID(ctx)
	order, err := c.repo.GetOrderByID(id)

	if err != nil {
		return utils.ErrorResponse(ctx, http.StatusBadRequest, err)
	}

	return ctx.JSON(http.StatusOK, order)
}

func (c *Controller) CreateOrder(ctx echo.Context) error {
	var order models.Order

	if err := ctx.Bind(&order); err != nil {
		return utils.ErrorResponse(ctx, http.StatusBadRequest, err)
	}

	newOrder, err := c.repo.CreateOrder(order)

	if err != nil {
		return utils.ErrorResponse(ctx, http.StatusInternalServerError, err)
	}

	return ctx.JSON(http.StatusCreated, newOrder)
}