package repositories

import (
	"server/models"
)

type MockRepositoryWithEmptyLists struct{}

func (m *MockRepositoryWithEmptyLists) GetOrders() ([]models.Order, error) {
	return []models.Order{}, nil
}
func (m *MockRepositoryWithEmptyLists) CreateOrder(order models.Order) (*models.Order, error) {
	return nil, nil
}

func (m *MockRepositoryWithEmptyLists) GetProducts() ([]models.Product, error) {
	return []models.Product{}, nil
}