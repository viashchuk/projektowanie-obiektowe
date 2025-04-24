package repositories

import (
	"time"
	"task-4/models"
)

func (r *Repository) SaveWeather(city string, temperature float64) error {
	w := models.Weather{
		City:        city,
		Temperature: temperature,
		Date:        time.Now(),
	}

	return r.DB.Create(&w).Error
}
