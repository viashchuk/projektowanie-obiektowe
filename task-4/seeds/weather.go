package seeds

import (
	"time"
	"task-4/models"
)

func (s *Seed) SeedWeather() {
	weather := []models.Weather{
		{City: "Berlin", Temperature: 15,   Date: time.Now()},
		{City: "Warsaw", Temperature: 18.3, Date: time.Now()},
		{City: "Paris",  Temperature: 20.1, Date: time.Now()},
		{City: "Rome",   Temperature: 23.7, Date: time.Now()},
		{City: "London", Temperature: 16.8, Date: time.Now()},
		{City: "Madrid", Temperature: 25.4, Date: time.Now()},
	}

	for _, w := range weather {
		s.DB.Save(&w)
	}
}
