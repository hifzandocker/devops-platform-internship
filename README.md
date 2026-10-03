# DevOps Platform Internship

Enterprise-style DevOps platform built during the Parallax Labs internship.

## Project Overview

This repository contains the complete implementation of the six-week DevOps internship project, including:

* Microservices
* Docker containers
* Kubernetes
* Terraform infrastructure
* Helm
* Service mesh and mTLS
* Kong API Gateway
* GitHub Actions CI
* ArgoCD GitOps CD
* Prometheus and Grafana observability
* Canary deployments and automated rollback

The project is maintained in a single GitHub repository throughout the internship.

## Repository Structure

```text
.
|-- README.md
|-- services/
|   |-- frontend/
|   `-- backend/
|-- docs/
|-- week-1/
|-- week-2/
|-- week-3/
|-- week-4/
|-- week-5/
|-- week-6/
|-- infra/
|-- k8s/
|-- gateway/
|-- observability/
`-- .github/
    `-- workflows/
```

## Prerequisites

The following tools have been installed and verified locally:

| Tool           | Version / Result |
| -------------- | ---------------- |
| WSL            | Version 2        |
| Docker Engine  | 29.4.0           |
| Docker Compose | v5.1.1           |
| kubectl        | v1.34.1          |
| Helm           | v4.3.0           |
| Terraform      | v1.16.4          |

### Docker Verification

Docker Engine was verified with:

```powershell
docker info --format '{{.ServerVersion}}'
```

Result:

```text
29.4.0
```

Docker was also tested with:

```powershell
docker run --rm hello-world
```

The test completed successfully.

### WSL Verification

WSL was checked with:

```powershell
wsl --list --verbose
```

Current result:

```text
NAME              STATE           VERSION
* docker-desktop  Running         2
```

## Week 1 Goals

* Build an independent frontend microservice.
* Build an independent backend microservice.
* Implement `/health` and `/info` endpoints.
* Run and test both services locally.
* Create optimized multi-stage Dockerfiles.
* Run containers as non-root user `1001`.
* Add `.dockerignore` files.
* Build and run both services locally with Docker.
* Document successful health checks and reproducible commands.

## Week 1 Implementation

### Architecture

```text
Developer
   |
   v
Git Repository
   |
   +-------------------+
   |                   |
   v                   v
Frontend Service    Backend Service
Port 8080           Port 8081
   |                   |
   +--------+----------+
            |
       Local Docker
       Containers
```

The frontend and backend are independent HTTP microservices.

The frontend listens on port `8080`.

The backend listens on port `8081`.

Each service provides `/health` and `/info` endpoints.

### Service Structure

```text
services/
|-- frontend/
|   |-- app.py
|   |-- Dockerfile
|   `-- .dockerignore
|
`-- backend/
    |-- app.py
    |-- Dockerfile
    `-- .dockerignore
```

### API Endpoints

| Service  | Endpoint  | Expected Result                           |
| -------- | --------- | ----------------------------------------- |
| Frontend | `/health` | HTTP 200 and `OK`                         |
| Frontend | `/info`   | HTTP 200 and frontend service information |
| Backend  | `/health` | HTTP 200 and `OK`                         |
| Backend  | `/info`   | HTTP 200 and backend service information  |

### Docker Implementation

Both services use multi-stage Dockerfiles.

Both services use the lightweight `python:3.14-slim` base image.

Both runtime containers run as non-root user `1001`.

Both services have a `.dockerignore` file.

### Build Images

Build the frontend image:

```powershell
docker build -t frontend:week1 .\services\frontend
```

Build the backend image:

```powershell
docker build -t backend:week1 .\services\backend
```

### Run Containers

Run the frontend:

```powershell
docker run -d --name frontend-week1 -p 8080:8080 frontend:week1
```

Run the backend:

```powershell
docker run -d --name backend-week1 -p 8081:8081 backend:week1
```

### Verify Health Endpoints

Frontend:

```powershell
curl.exe -i http://localhost:8080/health
```

Result:

```text
HTTP 200 OK
OK
```

Backend:

```powershell
curl.exe -i http://localhost:8081/health
```

Result:

```text
HTTP 200 OK
OK
```

### Verify Information Endpoints

Frontend:

```powershell
curl.exe -i http://localhost:8080/info
```

Result:

```text
{"service": "frontend", "version": "1.0.0"}
```

Backend:

```powershell
curl.exe -i http://localhost:8081/info
```

Result:

```text
{"service": "backend", "version": "1.0.0"}
```

### Container Security Verification

The configured Docker user was verified with:

```powershell
docker image inspect frontend:week1 --format '{{.Config.User}}'
docker image inspect backend:week1 --format '{{.Config.User}}'
```

Result:

```text
1001
1001
```

The running containers were also checked with:

```powershell
docker exec frontend-week1 id
docker exec backend-week1 id
```

Both containers run with UID `1001`.

### Week 1 Verification Record

Detailed Week 1 testing and Docker verification is recorded in:

`week-1/verification.md`

## Development Workflow

Changes are made locally and tracked with Git:

```text
Change files
git status
git add
git commit
git push
GitHub
```

## Security

Secrets, environment files, Terraform state, logs, temporary files, and other local/generated files are excluded through `.gitignore`.

Real passwords, API keys, access tokens, credentials, or other secrets must never be committed to this repository.
