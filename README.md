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

A test container was also successfully started with:

```powershell
docker run --rm hello-world
```

The Docker test confirmed that the Docker client can communicate with the Docker daemon, pull an image, create a container, and run it successfully.

### WSL Verification

WSL distributions were checked with:

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
