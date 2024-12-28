# Variables
DOCKER_COMPOSE = docker-compose
BACKEND_SERVICE = backend
FRONTEND_SERVICE = frontend

# Targets
.PHONY: help install build up down restart logs backend-logs frontend-logs clean

help:
	@echo "Available targets:"
	@echo "  install       - Install dependencies using Poetry"
	@echo "  build         - Build all Docker containers"
	@echo "  up            - Start all services"
	@echo "  down          - Stop all services"
	@echo "  restart       - Restart all services"
	@echo "  logs          - Show logs for all services"
	@echo "  backend-logs  - Show logs for the backend service"
	@echo "  frontend-logs - Show logs for the frontend service"
	@echo "  clean         - Remove all containers, volumes, and images"

install:
	@echo "Installing dependencies for backend..."
	cd backend && POETRY_VIRTUALENVS_IN_PROJECT=true poetry install
	@echo "Installing dependencies for frontend..."
	cd frontend && POETRY_VIRTUALENVS_IN_PROJECT=true poetry install

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

restart:
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) up -d

logs:
	$(DOCKER_COMPOSE) logs -f

backend-logs:
	$(DOCKER_COMPOSE) logs -f $(BACKEND_SERVICE)

frontend-logs:
	$(DOCKER_COMPOSE) logs -f $(FRONTEND_SERVICE)

clean:
	$(DOCKER_COMPOSE) down --volumes --rmi all
