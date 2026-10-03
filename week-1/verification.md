# Week 1 Verification

## Prerequisites

The following tools were installed and verified locally:

| Tool | Version / Result |
|---|---|
| WSL | Version 2 |
| Docker Engine | 29.4.0 |
| Docker Compose | v5.1.1 |
| kubectl | v1.34.1 |
| Helm | v4.3.0 |
| Terraform | v1.16.4 |

Docker Engine was verified with:

docker info --format '{{.ServerVersion}}'

Result:

29.4.0

Docker was also tested with:

docker run --rm hello-world

The test completed successfully.

## Frontend Service

Location:

services/frontend

Port:

8080

Endpoints:

GET /health
GET /info

Docker image:

frontend:week1

Docker run command:

docker run -d --name frontend-week1 -p 8080:8080 frontend:week1

Verification:

curl.exe -i http://localhost:8080/health
curl.exe -i http://localhost:8080/info

Results:

HTTP 200 OK

OK

{"service": "frontend", "version": "1.0.0"}

The running container was verified with:

docker exec frontend-week1 id

Result:

uid=1001(appuser) gid=1001(appuser) groups=1001(appuser)

## Backend Service

Location:

services/backend

Port:

8081

Endpoints:

GET /health
GET /info

Docker image:

backend:week1

Docker run command:

docker run -d --name backend-week1 -p 8081:8081 backend:week1

Verification:

curl.exe -i http://localhost:8081/health
curl.exe -i http://localhost:8081/info

Results:

HTTP 200 OK

OK

{"service": "backend", "version": "1.0.0"}

The running container was verified with:

docker exec backend-week1 id

Result:

uid=1001(appuser) gid=1001(appuser) groups=1001(appuser)

## Dockerfile Requirements

Both services use:

python:3.14-slim

Both Dockerfiles contain separate builder and runtime stages.

Both runtime containers use:

USER 1001

Both services have a .dockerignore file.

## Final Docker Verification

Frontend:

http://localhost:8080/health -> HTTP 200 OK
http://localhost:8080/info -> HTTP 200 OK

Backend:

http://localhost:8081/health -> HTTP 200 OK
http://localhost:8081/info -> HTTP 200 OK

Both services were successfully built as Docker images and started as containers.

## Reproducible Build Commands

Frontend:

docker build -t frontend:week1 .\services\frontend
docker run -d --name frontend-week1 -p 8080:8080 frontend:week1

Backend:

docker build -t backend:week1 .\services\backend
docker run -d --name backend-week1 -p 8081:8081 backend:week1

## Status

Week 1 service implementation and local Docker verification are complete.

The remaining Week 1 documentation work is to update the main README with the architecture diagram, service structure, build commands, and verification information.
