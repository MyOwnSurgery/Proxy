# Black Russia Proxy

## Start Application

### Image building
```
docker build -t proxy .
```

### App starting
```
docker run -p 80:8080 proxy
```

### App starting with env variables
```
docker run 
-e STRING_TO_REPLACE="Black Russia" 
-e STRING_TO_REPLACE_WITH="BlackHub Games" -p 80:8080 proxy
```
### You can see all the variables in Dockerfile

### Time spent
```
Regexes building ~ 2 hours
Selenium exploring ~ 2 hours
Building architecture and webapp itself ~ 3 hours
Testing and debugging ~ 3 hours
```

### Problems
```
Can`t cope with transparent images and svgs 
```