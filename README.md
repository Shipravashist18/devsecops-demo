# DevSecOps Demo Project

![DevSecOps](https://img.shields.io/badge/DevSecOps-Demo-blue)

## Overview
This is a **DevSecOps demo project** showcasing a full pipeline including:

- Containerized application (Python Flask)
- Kubernetes deployment
- CI/CD pipeline via GitHub Actions
- Monitoring using Prometheus & Grafana
- Basic security scanning with Trivy

The purpose of this project is to demonstrate **DevSecOps practices** in a real-world environment.

---

## Project Structure
.github/ # GitHub Actions workflow for CI/CD
app.py # Simple Python Flask app
Dockerfile # Docker image definition
deployment.yaml # Kubernetes Deployment manifest
service.yaml # Kubernetes Service manifest
prometheus-nodeport.yaml # Prometheus NodePort configuration
grafana-dashboard-provider.yaml # Grafana dashboard provider
grafana-datasource.yaml # Grafana datasource config
grafana-service.yaml # Grafana service manifest
networkpolicy.yaml # Example Kubernetes NetworkPolicy
k8s-dashboard.json # Grafana dashboard JSON (3662)


---

## Features

### Application
- `app.py` is a simple Flask app (`Hello DevSecOps`)
- Dockerized for container deployment

### Kubernetes
- Deployment and Service manifests to run the app in a cluster
- NodePort for external access
- Optional NetworkPolicy for security controls

### CI/CD Pipeline
- Automated build & push of Docker image using **GitHub Actions**
- Deployment to Kubernetes cluster after successful build

### Monitoring & Visualization
- **Prometheus** collects metrics from Kubernetes cluster
- **Grafana** visualizes metrics via imported dashboard (3662)
- Node Exporter collects node-level metrics (some metrics may show `NA` on Docker Desktop)

### Security
- **Trivy** scans Docker images for vulnerabilities

---

## How to Run

1. Clone the repo

git clone https://github.com/Shipravashist18/devsecops-demo.git
cd devsecops-demo


2. Build Docker Image
docker build -t shipravashist/devsecops-demo:v3 .


3. Deploy to Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml


4. Deploy Prometheus & Grafana
kubectl apply -f prometheus-nodeport.yaml
kubectl apply -f grafana-service.yaml
kubectl apply -f grafana-datasource.yaml
kubectl apply -f grafana-dashboard-provider.yaml


5. Access services

Grafana → NodePort (default 3000)
Prometheus → NodePort (default 30001)
App → NodePort (default 30007)


Notes 

->Dashboard imported: 3662 (Cluster & Pod metrics)
->Some Node metrics may be NA due to Docker Desktop limitations
->CI/CD workflow is defined in .github/workflows/docker-ci.ym

Skills Demonstrated
1. Docker & containerization
2. Kubernetes deployments and services
3. CI/CD pipelines (GitHub Actions)
4. Monitoring & visualization (Prometheus + Grafana)
5. Basic security scanning (Trivy)
6. DevSecOps practices




Automate dashboard provisioning with Helm.
