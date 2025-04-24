package controllers

import(
	"task-4/repositories"
)

type Controller struct {
	repo *repositories.Repository
}

func NewController(repo *repositories.Repository) *Controller {
	return &Controller{repo: repo}
}
