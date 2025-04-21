package repositories

import (
	"fmt"
	"server/models"
)

func (r *Repository) GetOrders() ([]models.Order, error) {
	var orders []models.Order
	err := r.DB.Preload("OrderItems.Product").Find(&orders).Error
	return orders, err
}

func (r *Repository) GetOrderByID(id int) (*models.Order, error) {
	var order models.Order

	if err := r.DB.Preload("OrderItems.Product").First(&order, id).Error; err != nil {
		return nil, fmt.Errorf("order not found")
	}

	return &order, nil
}

func (r *Repository) CreateOrder(o models.Order) (*models.Order, error) {
	for i := range o.OrderItems {
		o.OrderItems[i].OrderID = uint(o.ID)
	}

	if err := r.DB.Create(&o).Error; err != nil {
		return nil, err
	}
	
	r.DB.Preload("OrderItems.Product").First(&o, o.ID)

	return &o, nil
}
