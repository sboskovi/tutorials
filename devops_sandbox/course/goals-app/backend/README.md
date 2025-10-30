# Docker commands
## Create network
docker network create goals-net

## Run mongo DB
docker run --name mongodb -d --rm -v mongo-data:/data/db --network goals-net mongo

## Run mongo DB with set username and password
docker run --name mongodb -v data:/data/db --rm -d --network goals-net -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=root mongo

## Build backend
docker build -t goals-node .

## Run backend
docker run --name goals-backend -d --rm --network goals-net -p 80:80 goals-node

## Run backend with bind mount
docker run -d --rm --name goals-backend -v /mnt/c/code/tutorials/devops_sandbox/course/goals-app/backend:/app -v logs:/app/logs -v /app/node_modules --network goals-net -p 80:80 goals-node

## Run frontend
docker run --name goals-frontend --rm -p 3000:3000 -it goals-react

## Run frontend with bind mount
docker run --name goals-frontend -v /mnt/c/code/tutorials/devops_sandbox/course/goals-app/frontend/src:/app/src --rm -p 3000:3000 -it goals-react