package config

import (
	"github.com/spf13/viper"
)

func LoadConfig() {
	viper.SetConfigFile(".env")
	viper.SetConfigType("env")
	viper.AutomaticEnv()

	err := viper.ReadInConfig()
    if err != nil {
        return
    }
}
func GetOpenWeatherApiKey() string {
	return viper.GetString("OPENWEATHER_API_KEY")
}

func GetOpenWeatherBaseUrl() string {
	return viper.GetString("OPENWEATHER_BASE_URL")
}