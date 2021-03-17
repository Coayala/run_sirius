# Docker container for running SIRIUS

This is a docker container to run [SIRIUS](https://bio.informatik.uni-jena.de/software/sirius/)

This container is intended to be run on the Cyberse data workbench

# Instructions

## 1. Pull the container from [DockerHub](https://hub.docker.com/repository/docker/coayala/run_sirius/general)

```
docker pull coayala/run_sirius:latest
```

## 2. Run the container 

```
docker run -it -p 8888:8888 coayala/run_sirius:test
```

