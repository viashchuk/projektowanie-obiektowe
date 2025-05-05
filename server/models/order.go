package models

import (
	"gorm.io/gorm"
)

type Order struct {
	gorm.Model
	OrderItems        []OrderItem `json:"items" gorm:"foreignKey:OrderID"`
    CustomerFirstName string `json:"customerFirstName"`
    CustomerLastName  string `json:"customerLastName"`
    CustomerEmail     string `json:"customerEmail"`
    CardNumber        string `json:"-"`
    ExpiryMonth       string `json:"-"`
    ExpiryYear        string `json:"-"`
    CVC               string `json:"-"`
}