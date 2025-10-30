# Help
`docker command --help`

# Build docker image
`docker build .`

`docker build -t name_of_image .`

# Run docker container attached to output
`docker run image_id`

## attached to both output and allowing input -interactive -tty shell
`docker run -i -t image_id`
or
`docker run -it image_id`
or
`docker start -a -i container_id`

## Detached mode of output
`docker run -d image_id`
or
`docker start image_id`

## Start stopped docker container
`docker start container_id`

## Attach to docker container
`docker attach container_id`

# Logs
`docker logs container_id`

## attach to Logs
`docker logs -f container_id`

# Useful flags
## Remove container when it stops
`--rm`

# Remove
## Container
`docker rm container_id`
## Image
`docker rmi image_id`

## All unused images
`docker prune images`

# Copy to container
### src can be in container or local file system
`docker cp src/. dst/`

# Naming containers
`docker run --name name:tag`

moze da se iskoristi da se napravi novi tag ka istom image-u koji ima drugo ime
`docker tag image_name`
`docker -t image_name`

# Volumes
Volume je folder ili fajl unutar Docker **container**-a koji se mapira na neki folder pod host OS-om.
Mozes da dodas vise volume-a: `-v ... -v ... -v ...`

`docker volume ls`

`docker volume inspect volume_name`

### Remove
```
docker volume rm volume_name
# Remove all
docker volume prune
```

## Anonymous volume
Anonymous volume sluzi da docker prioretitizuje neki path unutar container-a u odnosu na externe path-ove npr. Bind mount-ujes `C:\code\backend:/app/`, ali neces da ti se mapira **node_modules** sa host OS-a.

`docker run ... -v /app/node_modules/ -v ...`


### U image-u:
```
VOLUME ["/temp"]

docker run -v path_in_container
docker run -v /app/node_modules
```

## Named volume
I dalje ne znas gdje se nalazi Volume na host OS-u, ali ce 

```
docker run -v volume_name:path_in_container
# Example
docker run -v stored_files:/app/storage
```

## Bind mounts
Za razliku od volume-a, njima kontrolises gdje ce da se nalazi volume na host operativnom sistemu.
Fajlovi se mapiraju sa hosta u docker container pa je korisno za debgovanje.

Obrati paznju da ce ti Bind Mount **pregaziti** ono sto si iskopirao u container `COPY` komandom
iz Dockerfile-a. Za stvari kao sto su `/temp` ili `/node_modules` napravi anonimni volume da ti
bind mount ne bi mapirao i te stvari sa host-a. 

```
docker run -v host_os_path:/container_path
# example:
docker run -v C:\code\backend:/app/
```

### Make bind mount a read only volume
`docker run -v host_os_path:/container_path:ro`

### Shortcut
```
# Linux / MacOs
-v $(pwd):/app
# Windows
-v "%cd%":/app
```


# ARGuments and ENVironment variables
Argumenti se koriste u Dockerfile-u za build image-a. Ne mogu da se koriste za CMD u Dockerfile.
ENV se koriste u container-u.


## ENV
### Dockerfile
Ne upisuj secrete u Dockerfile, vec prosljedjuj prilikom docker run-a.
```
ENV name value
# example
ENV PORT 80
```
Docker run
```
docker run --env PORT=80
# or
docker run -e PORT=80
```

## ARG
```
ARG DEFAULT_PORT=80
ENV $DEFAULT_PORT
```
`Docker build -t image_name:tag --build-arg DEFAULT_PORT=8080 .`

# Network
```
# Create network
docker network create my-network

# List networks
docker network ls

# Run container with connection to network
docker run -d --name mongo_db --network my-network mongo
```

Use name of the container in docker network in connection strings:
`url = 'monogdb://mongo_db:27017/swfavourites'`

Network drivers se mogu konfigurisati za tip mreze, default je `brige`.


# Docker Compose
docker-compose up -d
### -v je za volume
docker-compose down [-v]


# Other
```
docker history image_name
```


# Kubernetes
// kubectl config set-context --current --namespace=minerva-services-dev

kubectl config get-contexts


k config use-context DEV

k get pods -o wide

// kubectl scale deployment compliance-minerva-rps-riskdatahandler-deployment --replicas 0

kubectl scale statefulset compliance-minerva-rps-screening-merged-statefulset --replicas 0
kubectl scale statefulset compliance-minerva-rps-riskdatahandler-statefulset --replicas 0

kubectl rollout restart deployment compliance-minerva-rps-riskdatahandler-deployment
kubectl get pod compliance-minerva-rps-riskdatahandler-deployment -o yaml | kubectl replace --force -f -

kubectl rollout restart statefulset compliance-minerva-rps-screening-merged-statefulset


kubectl get pods -o jsonpath="{.items[*].spec.containers[*].image}" | tr -s '[[:space:]]' '\n' | sort | uniq


## Remove kubecl cache if you auth with non admin account 
rm -rf ~/.kube/cache/


# WSL
Get-NetAdapter | Where-Object {$_.InterfaceDescription -Match "Cisco AnyConnect"} | Set-NetIPInterface -InterfaceMetric 6000


docker pull postgres
docker run --name my-postgres -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres