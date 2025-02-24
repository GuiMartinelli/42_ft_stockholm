# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: guferrei <guferrei@student.42sp.org.br>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/02/14 21:33:23 by guferrei          #+#    #+#              #
#    Updated: 2025/02/24 17:38:03 by guferrei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

COMPOSE = docker compose
DOCKER-COMPOSE = -f infra/docker-compose.yml
DOCKER_FLAGS = up -d --build
DOCKER_STOP = down
DOCKER_IMAGES = image prune -a
DOCKER_SYSTEM = system prune -f

all: docker

docker:
	$(COMPOSE) $(DOCKER-COMPOSE) $(DOCKER_FLAGS)

stop:
	$(COMPOSE) $(DOCKER-COMPOSE) $(DOCKER_STOP)

clean:
	docker $(DOCKER_IMAGES) && docker $(DOCKER_SYSTEM)

