package controllers

import (
	"server/repositories"
)

type Controller struct {
	repo repositories.IRepository
}

func NewController(repo repositories.IRepository) *Controller {
	return &Controller{repo: repo}
}
