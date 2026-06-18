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

## Architecture

```text
                           GitHub Repository
                                   │
                                   ▼
                          GitHub Actions CI
                                   │
                                   ▼
                         AWS EC2 Infrastructure
                                   │
             ┌─────────────────────┼─────────────────────┐
             │                     │                     │
             ▼                     ▼                     ▼
      Flask Application      PostgreSQL DB       Prometheus
             │                                       │
             └─────────────────────┬─────────────────┘
                                   ▼
                               Grafana
                                   │
                                   ▼
                          Monitoring Dashboards


Application:
http://localhost:5000