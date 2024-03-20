#!make
include .env
SHELL:=/bin/bash

SED?=$(shell command -v gsed || command -v sed)

all: greet vault-start vault-configure

greet:
	$(info Oh, its you again!)

build-ansible-image:
	$(info Building Ansible Image ...)
	docker build -t allheads-vault-app-ansible:alpine -f containers/ansible/Dockerfile .

build-ansible-image-no-cache:
	$(info Building Ansible Image --no-cache ...)
	docker build --no-cache --progress plain -t allheads-vault-app-ansible:alpine -f containers/ansible/Dockerfile .

clean: vault-clean
	@rm -rf .env

env-test:
	@echo "VAULT_CE_VERSION=$(VAULT_CE_VERSION)"

env-check: 
	@if [ ! -f .env ]; then echo -e "Seems you are missing '.env' file.\nRun 'cp .env.default .env' to create one..."; exit 1; fi

vault-start:
	$(info Starting Vault ...)
	@docker compose -f containers/vault/docker-compose.yml --env-file .env up -d

vault-configure: build-ansible-image
	$(info Configuring Vault ...)
	@docker run --rm -it --name allheads-vault-app-ansible -v ${PWD}/containers/vault:/vault -v ${PWD}/.env:/vault/.env --network=vault-network allheads-vault-app-ansible:alpine ansible-playbook /vault/playbooks/main.yml

vault-clean: 
	@docker compose -f containers/vault/docker-compose.yml --env-file .env down
	@rm -rf containers/vault/.init_tokens containers/vault/.env volumes/vault/data volumes/vault/logs volumes/vault/policies

build-backend-image:
	$(info Building Backend Image ...)
	@docker build --no-cache -t allheads-vault-app-backend:python -f containers/backend/Dockerfile .

backend-start: build-backend-image
	$(info Starting Backend ...)
	@docker run -d --rm -p 5001:5001 --name allheads-vault-app-backend --env-file .env allheads-vault-app-backend:python

backend-stop: 
	@docker stop allheads-vault-app-backend
	@docker rmi allheads-vault-app-backend:python

develop: build-backend-image
	$(info Starting Backend Development...)
	@docker run -it --rm -p 5001:5001 --network=vault-network --name allheads-vault-app-develop -v ${PWD}/backend:/usr/src/app --env-file .env allheads-vault-app-backend:python python -m flask run --debug --host=0.0.0.0 --port=5001
