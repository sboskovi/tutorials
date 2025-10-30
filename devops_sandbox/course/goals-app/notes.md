# Aplikacija 
Sastoji se od:
  1. monogdb baze
  2. node backend-a
  3. react frontend-a


# Bitne komande

## Build images
  ### Backend
  docker build -t goals-node .

  ### Frontend
  docker build -t goals-react .

## Run images
  ### MongoDB
  docker run --name mongodb --rm -d -p 27017:27017 mongo
  or
  docker run --name mongodb --rm -d --network goals-net mongo

  #### Da bi sacuvali podatke nakon restarta mongodb container-a dodajemo `data` **named volume**.
  docker run --name mongodb -v data:/data/db/ --rm -d --network goals-net mongo

  #### Da proslijedimo authetifikacione podatke mongo image-u
    docker run --name mongodb -v data:/data/db/ --rm -d --network goals-net -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=root mongo

    U ovom slucaju moramo da modifikujemo connection string:
    mongodb://username:password@mongodb:27017/course-goals?authSource=admin


  ### Backend
  docker run --name goals-backend --rm -d -p 80:80 goals-node
  or
  docker run --name goals-backend --rm -d --network goals-net -p 80:80 goals-node

  Moramo da expose-ujemo port 80 i kad specificiramo mrezu da bi frontend mogao da vidi backend na portu 80 na localhost-u jer se fronted izvrsava iz browser-a, ne iz container-a.
  `goals-backend` je naziv container-a, `goals-node` image-a

  #### Bind Mount code for live updated, save logs to logs volume
    docker run --name goals-backend -v C:/code/.../backend:/app -v logs:/app/logs -v /app/node_modules -d --rm -p 80:80 --network goals-net goals-node

  ### Fronted
  docker run --name goals-frontend --rm -p 3000:3000 -it goals-react

  Frontend se izvrsava u browser-u tako da on treba da gadja URL koji je localhost. Pod predpostavkom da backend trci na localhost-u i da je expose-ovan na portu 80.
  Flag -it je neophodan jer frontend aplikacija ocekuje input signal. Ako ga ne dobije odmah izadje iz container-a.


## Network
docker network ls
docker network create goals-net

# Napoemene:
`EXPOSE PORT`  u docker fajlu ne radi nista - sluzi u dokumentacione svrhe

  ## Networking
  `host.docker.internal` je URL interne docker-ove mreze koja se ne bi trebalo da se koristi - moze za testiranje

  Ako je container-u specificirana mreza prilikom pokretanja onda je dovoljno u URL-ovima staviti naziv container-a da bi mogli da mu pristupimo iz drugih container-a.
