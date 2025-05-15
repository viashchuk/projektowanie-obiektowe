package repositories

import (
	"server/models"
)

func (r *Repository) GetOrders() ([]models.Order, error) {
	var orders []models.Order
	err := r.DB.Preload("OrderItems.Product").Find(&orders).Error
	return orders, err
}

func (r *Repository) CreateOrder(o models.Order) (*models.Order, error) {
	for i := range o.OrderItems {
		o.OrderItems[i].OrderID = o.ID
	}

	if err := r.DB.Create(&o).Error; err != nil {
		return nil, err
	}
	
	r.DB.Preload("OrderItems.Product").First(&o, o.ID)

	return &o, nil
}
