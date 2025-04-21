package controllers

import (
	"server/repositories"
)

type Controller struct {
	repo *repositories.Repository
}

func NewController(repo *repositories.Repository) *Controller {
	return &Controller{repo: repo}
}
