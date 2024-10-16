# build image
```
docker image build . -t sample-webserver-image
```

# run container
```
docker run --name sample-webserver-container -p 8080:8080 sample-webserver-image
```
docker run --name sample-webserver-container sample-webserver-image

# test sample-webserver-container
## case1
```
curl -X GET http://localhost:8080
```

## case2
```
curl -X POST http://localhost:8080 -d 'test'
```
