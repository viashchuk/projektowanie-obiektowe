package repositories

import (
	"fmt"
	"server/models"
)

func (r *Repository) GetProducts() ([]models.Product, error) {
	var products []models.Product
	err := r.DB.Find(&products).Error
	return products, err
}

func (r *Repository) GetProductByID(id int) (*models.Product, error) {
	var product models.Product

	if err := r.DB.First(&product, id).Error; err != nil {
		return nil, fmt.Errorf("product not found")
	}

	return &product, nil
}
