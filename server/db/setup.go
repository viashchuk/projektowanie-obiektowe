package db

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"

	"server/models"
)

func InitDB() *gorm.DB {
	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	db.AutoMigrate(&models.Product{}, &models.Order{}, &models.OrderItem{})

	return db
}
