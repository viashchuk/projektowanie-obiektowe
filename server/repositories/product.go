package repositories

import (
	"server/models"
)

func (r *Repository) GetProducts() ([]models.Product, error) {
	var products []models.Product
	err := r.DB.Find(&products).Error
	return products, err
}