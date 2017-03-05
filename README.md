# Dump HTTP request and environment for testing/debugging

- https://hub.docker.com/r/onjin/test-http

# Usage

Build your own:

```
docker build -t test-app .  # or make test-app
```

Use this version from docker hub:

```
docker run -it --rm -p 8888:8888 test-app
```
