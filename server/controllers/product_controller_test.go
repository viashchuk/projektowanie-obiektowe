package controllers

import (
	"net/http"
	"net/http/httptest"
	"server/controllers"
	"server/repositories"
	"testing"

	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
)

func setupEcho() *echo.Echo {
	return echo.New()
}

func TestGetProducts_Success(t *testing.T) {
	e := echo.New()
	req := httptest.NewRequest(http.MethodGet, "/products", nil)
	rec := httptest.NewRecorder()
	ctx := e.NewContext(req, rec)

	MockRepository := &repositories.MockRepository{}
	ctrl := controllers.NewController(MockRepository)

	err := ctrl.GetProducts(ctx)

	assert.NoError(t, err)
	assert.Equal(t, http.StatusOK, rec.Code)
	assert.Contains(t, rec.Body.String(), "Kawa")
}

func TestGetProducts_EmptyList(t *testing.T) {
	e := echo.New()
	req := httptest.NewRequest(http.MethodGet, "/products", nil)
	rec := httptest.NewRecorder()
	ctx := e.NewContext(req, rec)

	mockRepository := &repositories.MockRepositoryWithEmptyLists{}
	ctrl := controllers.NewController(mockRepository)

	err := ctrl.GetProducts(ctx)

	assert.NoError(t, err)
	assert.Equal(t, http.StatusNoContent, rec.Code)
}