package seeds

import (
	"server/models"
)

func (s *Seed) SeedProducts() {
	products := []models.Product{
		{Title: "Kenia Githaiti", Price: 65, Amount: 19, ImageURL: "uploads/products/kenia_githaiti.webp", Description: "MIÓD · CYTRYNA · GRANAT · RABARBAR"},
		{Title: "Kolumbia El Rincon", Price: 67, Amount: 10, ImageURL: "uploads/products/kolumbia.webp", Description: "DOJRZAŁE MANGO · JAGODY · RUM · CIEMNA CZEKOLADA"},
		{Title: "Kenia Kiboko decaf", Price: 72, Amount: 1000, ImageURL: "uploads/products/kenia_decaf.webp", Description: "SŁODKA POMARAŃCZA · MELASA · CYTRUSY"},
		{Title: "Honduras Carlos Ulloa", Price: 79, Amount: 100, ImageURL: "uploads/products/honduras.webp", Description: "DŻEM PORZECZKOWY · TRUSKAWKA · POMARAŃCZA · KARMEL"},
		{Title: "Smooth Sweet", Price: 52, Amount: 100, ImageURL: "uploads/products/smooth_sweet.webp", Description: "SŁODKA TRUSKAWKA · CZEKOLADA · MALINA · RÓŻA"},
		{Title: "Floral Essence", Price: 52, Amount: 100, ImageURL: "uploads/products/floral_essence.webp", Description: "KWIATY · KANDYZOWANA CYTRYNA · MLECZNA CZEKOLADA"},
		{Title: "Juicy Blast", Price: 52, Amount: 100, ImageURL: "uploads/products/juicy_blast.webp", Description: "GREJPFRUT · KAKAO · DŻEM PORZECZKOWY"},
		{Title: "Intense", Price: 32, Amount: 100, ImageURL: "uploads/products/intense.webp", Description: "CIEMNA CZEKOLADA · MIGDAŁY"},
		{Title: "Smooth Sweet kapsułki", Price: 30, Amount: 100, ImageURL: "uploads/products/smooth_sweet_kap.webp", Description: "SŁODKA TRUSKAWKA · CZEKOLADA · MALINA · RÓŻA"},
		{Title: "Honduras Marcala kapsułki", Price: 28, Amount: 100, ImageURL: "uploads/products/honduras_kap.webp", Description: "CUKIER TRZCINOWY · CZEKOLADA · ORZECH"},
		{Title: "Chocolate Bomb kapsułki", Price: 29, Amount: 100, ImageURL: "uploads/products/chocolate.webp", Description: "CZEKOLADA DESEROWA · KAKAO · ORZECHY"},
		{Title: "Etiopia Oromia kapsułki", Price: 31, Amount: 100, ImageURL: "uploads/products/etiopia.webp", Description: "MIÓD · BRZOSKWINIA · CZERWONA PORZECZKA"},
	}

	for _, product := range products {
		s.DB.Save(&product)
	}
}