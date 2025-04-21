package models

import (
	"gorm.io/gorm"
)

type Order struct {
	gorm.Model
    ID        int       `json:"id"`
	Items []Product `gorm:"many2many:order_items;" json:"items"`
    CustomerFirstName string `json:"firstName"`
    CustonerLastName  string `json:"lastName"`
    CustomerEmail  string `json:"email"`
    CardNumber     string `json:"cardNumber"`
    ExpiryMonth    string `json:"expiryMonth"`
    ExpiryYear     string `json:"expiryYear"`
    CVC            string `json:"cvc"`
}