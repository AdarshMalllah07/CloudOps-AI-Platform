![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-WebApp-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue)
![Helm](https://img.shields.io/badge/Helm-Package%20Manager-blue)
![ArgoCD](https://img.shields.io/badge/ArgoCD-GitOps-orange)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-orange)
![Grafana](https://img.shields.io/badge/Grafana-Observability-red)

# CloudOps AI Platform

![CI](https://github.com/AdarshMalllah07/CloudOps-AI-Platform/actions/workflows/ci.yml/badge.svg)

## Overview

CloudOps AI Platform is an AI-powered CloudOps and SRE automation platform designed to demonstrate modern cloud-native infrastructure management, GitOps deployment practices, observability, automated recovery, and operational intelligence.

The platform combines Kubernetes, GitOps, Infrastructure as Code, monitoring, alerting, and self-healing automation into a single operational workflow.

---

## Key Features

### Cloud Infrastructure

- Infrastructure provisioning using Terraform
- AWS EC2 deployment environment
- PostgreSQL database integration
- Containerized application deployment using Docker

### Kubernetes & GitOps

- Kubernetes-based workload orchestration
- Helm package management
- ArgoCD GitOps deployment workflow
- Kubernetes Ingress configuration
- Horizontal Pod Autoscaling (HPA)
- ConfigMap and Secret management

### Observability & Monitoring

- Prometheus metrics collection
- Grafana dashboards
- Node Exporter system monitoring
- Kubernetes Metrics Server
- Prometheus alert rules
- Infrastructure health monitoring

### AI Operations & Automation

- AI-powered incident analysis
- Infrastructure health recommendations
- Automated recovery actions
- Kubernetes self-healing workflows
- Webhook-driven remediation
- Auto-scaling based recovery actions

---

## Architecture Diagram

![Architecture Diagram](screenshots/CloudOps%20AI%20platform%20Architecture%20diagram.png)

---

## End-to-End Platform Flow

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
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
    ▼
CloudOps Application
    │
    ▼
Prometheus Monitoring
    │
    ▼
Grafana Dashboards
    │
    ▼
AI Incident Analysis
    │
    ▼
Self-Healing Automation
```

---

## GitOps Deployment Workflow

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
GitHub Actions
    │
    ▼
ArgoCD
    │
    ▼
Helm Charts
    │
    ▼
Kubernetes Cluster
    │
    ▼
Application Deployment
```

---

## Automated Self-Healing Workflow

```text
Prometheus Alert
        │
        ▼
Alert Webhook
        │
        ▼
AI Incident Analyzer
        │
        ▼
Recovery Engine
        │
 ┌──────┴──────┐
 ▼             ▼

Scale Pods   Restart Workload
        │
        ▼
Kubernetes Recovery
```

---

## Technology Stack

| Category | Technologies |
|-----------|-------------|
| Backend | Flask, Python |
| Database | PostgreSQL |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes |
| Package Management | Helm |
| GitOps | ArgoCD |
| Infrastructure as Code | Terraform |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Cloud Platform | AWS EC2 |
| Observability | Node Exporter, Metrics Server |
| Automation | Self-Healing Engine |

---

## Kubernetes Components

| Component | Purpose |
|------------|----------|
| Deployment | Application Deployment |
| Service | Service Exposure |
| Ingress | Traffic Routing |
| HPA | Automatic Scaling |
| ConfigMap | Configuration Management |
| Secret | Sensitive Configuration |
| Helm | Package Management |
| ArgoCD | GitOps Automation |

---

## Service Endpoints

| Service | URL |
|----------|------|
| Application | http://localhost:5000 |
| Grafana | http://localhost:3000 |
| Prometheus | http://localhost:9090 |

---

## Key Achievements

- Built a cloud-native application platform on Kubernetes
- Implemented GitOps deployment workflows using ArgoCD
- Provisioned infrastructure using Terraform and AWS
- Automated CI/CD pipelines with GitHub Actions
- Configured Kubernetes Ingress and HPA
- Integrated Prometheus and Grafana for observability
- Developed AI-powered incident analysis workflows
- Implemented automated self-healing and recovery actions
- Built webhook-based Kubernetes remediation workflows
- Demonstrated end-to-end DevOps and SRE practices

---

## Future Enhancements

- Slack-based operational notifications
- Advanced AI root cause analysis
- AlertManager integration
- Multi-environment deployment strategy
- EKS deployment support

---

## Author

**Adarsh Mallah**

Cloud / DevOps Engineer Portfolio Project