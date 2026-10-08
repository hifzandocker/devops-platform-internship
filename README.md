# DevOps Platform Internship

Enterprise-style DevOps platform being developed during the Parallax Labs DevOps Engineering Internship.

This repository is the single GitHub repository used throughout the internship. Work is added progressively to the same repository each week.

## Current Status

**Week 1 — Complete**

Week 1 establishes the microservice and Docker foundation for the project.

## Repository Structure

```text
.
|-- README.md
|-- services/
|   |-- frontend/
|   |   |-- app.py
|   |   |-- Dockerfile
|   |   `-- .dockerignore
|   |
|   `-- backend/
|       |-- app.py
|       |-- Dockerfile
|       `-- .dockerignore
|
|-- docs/
|-- week-1/
|   `-- verification.md
|-- week-2/
|-- week-3/
|-- week-4/
|-- week-5/
|-- week-6/
|-- infra/
|-- k8s/
|-- gateway/
|-- observability/
|
`-- .github/
    `-- workflows/
```

`services/` contains the microservice source code.

`week-1/verification.md` contains the detailed Week 1 verification record.

The remaining directories are reserved for work that will be added during later weeks.

## Prerequisites

The following tools were installed and verified during Week 1:

| Tool           | Version / Result |
| -------------- | ---------------- |
| WSL            | Version 2        |
| Docker Engine  | 29.4.0           |
| Docker Compose | v5.1.1           |
| kubectl        | v1.34.1          |
| Helm           | v4.3.0           |
| Terraform      | v1.16.4          |

### WSL

Verified with:

```powershell
wsl --list --verbose
```

Result:

```text
NAME              STATE           VERSION
* docker-desktop  Running         2
```

### Docker

Verified with:

```powershell
docker info --format '{{.ServerVersion}}'
```

Result:

```text
29.4.0
```

Docker was also verified with:

```powershell
docker run --rm hello-world
```

### Docker Compose

```powershell
docker compose version
```

Result:

```text
Docker Compose version v5.1.1
```

### kubectl

```powershell
kubectl version --client
```

Verified:

```text
Client Version: v1.34.1
Kustomize Version: v5.7.1
```

### Helm

```powershell
helm version
```

Verified:

```text
v4.3.0
```

### Terraform

```powershell
terraform version
```

Verified:

```text
Terraform v1.16.4
```

## Week 1 Architecture

The Week 1 implementation consists of two independent HTTP microservices running as Docker containers.

```text
                         Developer
                            |
                            v
                     GitHub Repository
                            |
                 +----------+----------+
                 |                     |
                 v                     v
          Frontend Service      Backend Service
             Port 8080             Port 8081
                 |                     |
                 v                     v
          Docker Container      Docker Container
             UID 1001              UID 1001
```

The frontend and backend are independent HTTP microservices.

## Frontend

Location:

```text
services/frontend/
```

The frontend listens on port `8080`.

### Endpoints

`GET /health`

Verified result:

```text
HTTP 200 OK
OK
```

`GET /info`

Verified result:

```json
{"service": "frontend", "version": "1.0.0"}
```

## Backend

Location:

```text
services/backend/
```

The backend listens on port `8081`.

### Endpoints

`GET /health`

Verified result:

```text
HTTP 200 OK
OK
```

`GET /info`

Verified result:

```json
{"service": "backend", "version": "1.0.0"}
```

## Docker Implementation

Both services use:

* Multi-stage Dockerfiles
* `python:3.14-slim`
* Non-root runtime user `1001`
* `.dockerignore`

## Build

Run these commands from the repository root.

### Frontend

```powershell
docker build -t frontend:week1 .\services\frontend
```

### Backend

```powershell
docker build -t backend:week1 .\services\backend
```

## Run

### Frontend

```powershell
docker run -d --name frontend-week1 -p 8080:8080 frontend:week1
```

### Backend

```powershell
docker run -d --name backend-week1 -p 8081:8081 backend:week1
```

## Verification

### Frontend

```powershell
curl.exe -i http://localhost:8080/health
curl.exe -i http://localhost:8080/info
```

Verified `/health` response:

```text
HTTP 200 OK
OK
```

Verified `/info` response:

```json
{"service": "frontend", "version": "1.0.0"}
```

### Backend

```powershell
curl.exe -i http://localhost:8081/health
curl.exe -i http://localhost:8081/info
```

Verified `/health` response:

```text
HTTP 200 OK
OK
```

Verified `/info` response:

```json
{"service": "backend", "version": "1.0.0"}
```

## Container User Verification

The configured Docker user was verified with:

```powershell
docker image inspect frontend:week1 --format '{{.Config.User}}'
docker image inspect backend:week1 --format '{{.Config.User}}'
```

Verified result:

```text
1001
1001
```

The running containers were also checked with:

```powershell
docker exec frontend-week1 id
docker exec backend-week1 id
```

The containers were verified to run with UID `1001`.

## Week 1 Verification Record

Detailed verification evidence is available in:

```text
week-1/verification.md
```

It records the prerequisite checks, Docker builds, container execution, endpoint tests, and non-root user verification completed during Week 1.

## Cleanup

Stop and remove the Week 1 containers:

```powershell
docker rm -f frontend-week1 backend-week1
```

Remove the local images if no longer needed:

```powershell
docker rmi frontend:week1 backend:week1
```

## Development Workflow

Changes are made locally and tracked with Git.

```powershell
git status
git add .
git commit -m "description of change"
git push
```

The same GitHub repository will be used throughout the internship.

## Security

The repository uses `.gitignore` to exclude common generated and sensitive local files.

Real passwords, API keys, access tokens, credentials, and other secrets must never be committed to the repository.
