package models

import (
	"gorm.io/gorm"
)

type Order struct {
	gorm.Model
	OrderItems        []OrderItem `json:"items" gorm:"foreignKey:OrderID"`
    CustomerFirstName string `json:"firstName"`
    CustonerLastName  string `json:"lastName"`
    CustomerEmail     string `json:"email"`
    CardNumber        string `json:"cardNumber"`
    ExpiryMonth       string `json:"expiryMonth"`
    ExpiryYear        string `json:"expiryYear"`
    CVC               string `json:"cvc"`
}