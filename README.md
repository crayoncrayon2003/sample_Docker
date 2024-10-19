# Common
## containers
### show containers
```
docker ps -a
```

### run container
```
docker run --name <container name> <image name>
```

# enter the container
## exec
```
docker exec -it <container name> bash
```

### stop container
```
docker stop <container name>
```

### remove the container
```
docker rm <container name>
```

## images
### show images
```
sudo docker images
```

### remove the image
```
docker rmi <image name>
```

### network
## show network
```
docker network ls
```

### remove the network
```
docker network rm <Networ Name>
```

# Dokcer File
## build image
```
sudo docker build <Dokcer FileName> -t <image name>
```

# Dokcer Compose
## build and run
```
docker compose up -d
```

## show container
```
docker compose ps -a
```

## stop
```
docker compose down
```

# Others
## case :  memory is insufficient
```
ulimit -n 25536 in /etc/init.d/docker
```

## case :  garbage cleaning
```
docker container prune -f
docker image prune -a -f
docker volume prune -a -f
docker builder prune -a -f
docker system prune -a -f --volumes
```