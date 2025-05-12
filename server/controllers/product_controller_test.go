package controllers

import (
	"net/http"
	"net/http/httptest"
	"server/repositories"
	"testing"

	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
)

func TestGetProductsSuccess(t *testing.T) {
	e := echo.New()
	req := httptest.NewRequest(http.MethodGet, "/products", nil)
	rec := httptest.NewRecorder()
	ctx := e.NewContext(req, rec)

	MockRepository := &repositories.MockRepository{}
	ctrl := NewController(MockRepository)

	err := ctrl.GetProducts(ctx)

	assert.NoError(t, err)
	assert.Equal(t, http.StatusOK, rec.Code)
	assert.Contains(t, rec.Body.String(), "Kawa")
}

func TestGetProductsEmptyList(t *testing.T) {
	e := echo.New()
	req := httptest.NewRequest(http.MethodGet, "/products", nil)
	rec := httptest.NewRecorder()
	ctx := e.NewContext(req, rec)

	mockRepository := &repositories.MockRepositoryWithEmptyLists{}
	ctrl := NewController(mockRepository)

	err := ctrl.GetProducts(ctx)

	assert.NoError(t, err)
	assert.Equal(t, http.StatusNoContent, rec.Code)
}