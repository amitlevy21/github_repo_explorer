docker_compose_dev_up_cmd = docker-compose -f docker-compose.yml -f docker-compose.dev.yml
dev:
	$(docker_compose_dev_up_cmd) build
	$(docker_compose_dev_up_cmd) up

backend:
	$(docker_compose_dev_up_cmd) build repository db
	$(docker_compose_dev_up_cmd) up repository db

test:
	$(docker_compose_dev_up_cmd) build repository db
	$(docker_compose_dev_up_cmd) up -d db
	docker-compose run repository pytest
