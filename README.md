```md
![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-orange)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-red)

# CloudOps-AI-Platform

![CI](https://github.com/AdarshMalllah07/CloudOps-AI-Platform/actions/workflows/ci.yml/badge.svg)
CloudOps-AI-Platform


A cloud infrastructure management and monitoring platform built using Flask, PostgreSQL, Docker, Prometheus, Grafana, Terraform, GitHub Actions, and AWS.

## Overview

CloudOps AI Platform helps manage infrastructure environments, servers, and applications while providing monitoring, observability, and cloud deployment capabilities.

The platform demonstrates modern DevOps practices including:

- Infrastructure as Code (Terraform)
- Containerization (Docker)
- Monitoring (Prometheus)
- Visualization (Grafana)
- CI/CD (GitHub Actions)
- Cloud Deployment (AWS EC2)

---

## Service Endpoints

| Service | URL |
|----------|------|
| Flask Application | http://localhost:5000 |
| Grafana Dashboard | http://localhost:3000 |
| Prometheus | http://localhost:9090 |

## Architecture Diagram

![Architecture Diagram](screenshots/CloudOps%20AI%20platform%20Architecture%20diagram.png)


```text
                        GitHub Repository
                                │
                                ▼
                      GitHub Actions CI/CD
                                │
                                ▼
                           ArgoCD GitOps
                                │
                                ▼
                          Helm Charts
                                │
                                ▼
                     Kubernetes Cluster
                                │
        ┌───────────────┬───────────────┬───────────────┐
        │               │               │
        ▼               ▼               ▼
   Flask App      PostgreSQL DB    Node Exporter
        │
        ▼
   Prometheus
        │
        ▼
    Grafana
        │
        ▼
 AI Incident Analyzer

AWS Services:
- EC2
- CloudWatch
- SNS
```

### Infrastructure Components

| Component | Purpose |
|------------|----------|
| GitHub | Source code management |
| GitHub Actions | Continuous Integration & Deployment |
| Terraform | Infrastructure as Code provisioning |
| AWS EC2 | Cloud hosting environment |
| Docker Compose | Multi-container orchestration |
| Flask | Backend application and dashboard |
| PostgreSQL | Persistent data storage |
| Prometheus | Metrics collection and monitoring |
| Grafana | Visualization and dashboards |
| AI Incident Analysis | Automated infrastructure health recommendations |

### Deployment Flow

```text
Developer
    │
    ▼
Push Code to GitHub
    │
    ▼
GitHub Actions CI Pipeline
    │
    ▼
Automated Deployment to AWS EC2
    │
    ▼
Docker Compose Rebuild
    │
    ▼
Updated Application Available
```

### Monitoring Flow

```text
Application Metrics
        │
        ▼
   Prometheus
        │
        ▼
    Grafana
        │
        ▼
 Infrastructure Dashboard
        │
        ▼
 AI Incident Analysis
```

### Access Points

| Service | URL |
|----------|------|
| Flask Application | http://localhost:5000 |
| Grafana Dashboard | http://localhost:3000 |
| Prometheus | http://localhost:9090 |
| PostgreSQL | Internal Docker Network |

## Kubernetes Components

| Component | Purpose |
|------------|----------|
| Deployment | Application Deployment |
| Service | Internal/External Access |
| HPA | Auto Scaling |
| ConfigMap | Application Configuration |
| Secret | Sensitive Data Management |
| Helm | Kubernetes Package Management |
| ArgoCD | GitOps Deployment Automation |

## GitOps Workflow

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
ArgoCD
    │
    ▼
Helm Chart
    │
    ▼
Kubernetes Cluster
    │
    ▼
CloudOps Application
```

## Key Achievements

- Provisioned AWS Infrastructure using Terraform
- Infrastructure Provisioning using Terraform
- Containerized Deployment with Docker & Docker Compose
- Kubernetes Orchestration with Deployments and Services
- Horizontal Pod Autoscaling (HPA)
- Helm-based Kubernetes Package Management
- GitOps Deployment using ArgoCD
- CI/CD Automation with GitHub Actions
- PostgreSQL Database Integration
- Infrastructure Monitoring with Prometheus
- Visualization and Dashboards using Grafana
- Node Exporter System Metrics Collection
- AWS CloudWatch Monitoring
- AWS SNS Alert Notifications
- AI-Powered Incident Analysis Engine