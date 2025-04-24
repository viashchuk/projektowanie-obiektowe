package models

import (
	"time"
	"gorm.io/gorm"
)

type Weather struct {
	gorm.Model
	Date        time.Time
	Temperature float64
	City        string
}
