package controllers

import (
	"bytes"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"server/models"
	"server/repositories"
	"testing"

	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
)
const ordersPath = "/orders"

func TestGetOrdersSuccess(t *testing.T) {
	e := echo.New()
	req := httptest.NewRequest(http.MethodGet, ordersPath, nil)
	rec := httptest.NewRecorder()
	ctx := e.NewContext(req, rec)

	mockRepository := &repositories.MockRepository{}
	ctrl := NewController(mockRepository)

	err := ctrl.GetOrders(ctx)

	assert.NoError(t, err)
	assert.Equal(t, http.StatusOK, rec.Code)
}

func TestGetOrdersEmptyList(t *testing.T) {
	e := echo.New()
	req := httptest.NewRequest(http.MethodGet, ordersPath, nil)
	rec := httptest.NewRecorder()
	ctx := e.NewContext(req, rec)

	mockRepository := &repositories.MockRepositoryWithEmptyLists{}
	ctrl := NewController(mockRepository)

	err := ctrl.GetOrders(ctx)

	assert.NoError(t, err)
	assert.Equal(t, http.StatusNoContent, rec.Code)
}

func TestCreateOrderSuccess(t *testing.T) {
	e := echo.New()

	order := models.Order{
		CustomerFirstName: "Anna",
		CustomerLastName:  "Nowak",
		CustomerEmail:     "anna@example.com",
		CardNumber:        "4111111111111111",
		ExpiryMonth:       "12",
		ExpiryYear:        "25",
		CVC:               "123",
		OrderItems: []models.OrderItem{
			{ProductID: 1, Quantity: 2},
		},
	}

	body, _ := json.Marshal(order)
	req := httptest.NewRequest(http.MethodPost, ordersPath, bytes.NewReader(body))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	rec := httptest.NewRecorder()
	ctx := e.NewContext(req, rec)

	mockRepository := &repositories.MockRepository{}
	ctrl := NewController(mockRepository)

	err := ctrl.CreateOrder(ctx)

	assert.NoError(t, err)
	assert.Equal(t, http.StatusCreated, rec.Code)
}

func TestCreateOrderInvalidData(t *testing.T) {
	e := echo.New()

	req := httptest.NewRequest(http.MethodPost, ordersPath, bytes.NewBufferString("invalid-json"))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	rec := httptest.NewRecorder()
	ctx := e.NewContext(req, rec)

	mockRepository := &repositories.MockRepository{}
	ctrl := NewController(mockRepository)

	err := ctrl.CreateOrder(ctx)

	assert.NoError(t, err)
	assert.Equal(t, http.StatusBadRequest, rec.Code)
}

func TestCreateOrderEmptyItems(t *testing.T) {
	e := echo.New()

	body := `{
		"firstName": "Anna",
		"lastName": "Nowak",
		"email": "anna@example.com",
		"cardNumber": "4111111111111111",
		"expiryMonth": "12",
		"expiryYear": "25",
		"cvc": "123",
		"items": []
	}`

	req := httptest.NewRequest(http.MethodPost, ordersPath, bytes.NewBufferString(body))
	req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
	rec := httptest.NewRecorder()
	ctx := e.NewContext(req, rec)

	mockRepository := &repositories.MockRepository{}
	ctrl := NewController(mockRepository)

	err := ctrl.CreateOrder(ctx)

	assert.NoError(t, err)
	assert.Equal(t, http.StatusBadRequest, rec.Code)
}