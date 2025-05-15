package repositories

import (
	"server/models"
)

type MockRepository struct{}

func (m *MockRepository) GetOrders() ([]models.Order, error) {
	return []models.Order{{
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
	},}, nil
}

func (m *MockRepository) GetOrdersEmptyList() ([]models.Order, error) {
	return []models.Order{}, nil
}

func (m *MockRepository) CreateOrder(o models.Order) (*models.Order, error) {
	return &o, nil
}

func (m *MockRepository) GetProducts() ([]models.Product, error) {
	return []models.Product{
		{Title: "Kawa", Price: 10},
	}, nil
}