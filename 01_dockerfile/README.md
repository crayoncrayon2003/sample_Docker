# show containers
```
sudo docker images
```

# show images
```
sudo docker images
```

# show network
```
docker network ls
```


# build image
```
sudo docker build . -t my-ubuntu-image
```

# run container
```
docker run --name my-ubuntu-container my-ubuntu-image
```

# enter the container
## exec
```
docker exec -it my-ubuntu-container bash
```

## attach
```
docker attach my-ubuntu-container
```

# exit the container
## exec
```
exit
```

# stop the container
```
docker stop my-ubuntu-container
```

# remove the container
```
docker rm my-ubuntu-container
```

# remove the image
```
docker rmi my-ubuntu-image
```

# remove the network
```
docker network rm <Networ Name>
```