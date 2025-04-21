package seeds

import (
	"server/models"
)

func (s *Seed) SeedProducts() {
	products := []models.Product{
		{Title: "MacBook Air", Price: 7000, Amount: 1},
		{Title: "MacBook Pro", Price: 9000, Amount: 10},
		{Title: "iPhone 15", Price: 3000, Amount: 2},
	}

	for _, product := range products {
		s.DB.Save(&product)
	}
}
