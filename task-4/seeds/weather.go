package seeds

import (
	"time"
	"task-4/models"
)

func (s *Seed) SeedWeather() {
	weather := []models.Weather{
		{City: "Gdansk", Temperature: 15,   Date: time.Now()},
		{City: "Warsaw", Temperature: 18.3, Date: time.Now()},
		{City: "Krakow",  Temperature: 20.1, Date: time.Now()},
	}

	for _, w := range weather {
		s.DB.Save(&w)
	}
}
