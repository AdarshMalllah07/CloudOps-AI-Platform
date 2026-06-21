# CloudOps AI Platform Architecture

```text
User Browser
      |
      v
Flask Web Application
      |
      v
PostgreSQL Database

Future Integrations
-------------------
Docker
Prometheus
Grafana
Terraform
AWS
GitHub Actions
AI Engine
```

GitHub Repository
       │
       ▼
GitHub Actions
       │
       ▼
AWS EC2
       │
 Docker Compose
 ┌─────┼────────┬──────────┐
 ▼     ▼        ▼          ▼
Flask Postgres Prometheus Grafana
       │
       ▼
AI Incident Analysis Engine