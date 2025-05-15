package models

import (
	"gorm.io/gorm"
)

type Product struct {
	gorm.Model
	Title       string   `json:"title" gorm:"not null" validate:"required"`
	Price       int      `json:"price" gorm:"not null" validate:"required"`
	Amount      int      `json:"amount" gorm:"not null" validate:"required"`
	ImageURL    string  `json:"image_url" gorm:"default:null"`
	Description string
}
