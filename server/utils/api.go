package utils

import (
	"strconv"

	"github.com/labstack/echo/v4"
)

func ParseID(ctx echo.Context) (int, error) {
	return strconv.Atoi(ctx.Param("id"))
}

func ErrorResponse(ctx echo.Context, code int, err error) error {
	return ctx.JSON(code, echo.Map{
		"error": err.Error(),
	})
}
