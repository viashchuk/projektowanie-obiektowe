package services

import (
	"io"
	"fmt"
	"net/http"
	"encoding/json"

	"task-4/config"
	"task-4/repositories"
)

type WeatherSummary struct {
	City        string  `json:"city"`
	Temperature float64 `json:"temperature"`
}

func GetCityWeather(city string, repo *repositories.Repository) (*WeatherSummary, error) {
	apiKey := config.GetOpenWeatherApiKey()
	baseURL := config.GetOpenWeatherBaseUrl()

	url := fmt.Sprintf("%s?q=%s&appid=%s&units=metric", baseURL, city, apiKey)

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return nil, err
	}

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	var result map[string]interface{}
	if err := json.Unmarshal(body, &result); err != nil {
		return nil, fmt.Errorf("failed to parse JSON: %w", err)
	}

	temp := result["main"].(map[string]interface{})["temp"].(float64)

	_ = repo.SaveWeather(city, temp)

	return &WeatherSummary{
		City:        city,
		Temperature: temp,
	}, nil
}