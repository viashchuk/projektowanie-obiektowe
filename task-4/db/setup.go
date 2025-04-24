package db

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"

	"task-4/models"
)

func InitDB() *gorm.DB {
	db, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	db.AutoMigrate(&models.Weather{})

	return db
}
