package repositories

import "server/models"

type IRepository interface {
	GetOrders() ([]models.Order, error)
	CreateOrder(order models.Order) (*models.Order, error)

	GetProducts() ([]models.Product, error)
}