# 🚀 DevSecOps Project – Secure CI/CD with Kubernetes, Prometheus & Grafana

This project demonstrates a **DevSecOps pipeline** that integrates application development, security scanning, containerization, and monitoring using modern tools like **Docker, Kubernetes, Trivy, Prometheus, and Grafana**.

---

## 📌 Features
- ✅ **Python Application** (`app.py`) – Simple demo app containerized with Docker.  
- ✅ **CI/CD with GitHub Actions** – Automated build & push of Docker images.  
- ✅ **Container Security with Trivy** – Scans images for vulnerabilities.  
- ✅ **Kubernetes Deployment** – Secure pod deployment with `Deployment.yaml` and `Service.yaml`.  
- ✅ **Network Policies** – Restrict pod-to-pod communication.  
- ✅ **Monitoring with Prometheus** – Collects application & cluster metrics.  
- ✅ **Visualization with Grafana** – Real-time dashboards for monitoring app & infra.  

---

## 🛠️ Tech Stack
- **Language**: Python  
- **Containerization**: Docker  
- **Orchestration**: Kubernetes (K8s)  
- **Security**: Trivy (Image Scanning)  
- **CI/CD**: GitHub Actions  
- **Monitoring**: Prometheus  
- **Visualization**: Grafana  

---

## 📂 Repository Structure
├── app.py # Python application
├── Dockerfile # Docker build file
├── deployment.yaml # K8s Deployment
├── service.yaml # K8s Service (NodePort/ClusterIP)
├── networkpolicy.yaml # K8s Network Policy
├── grafana-datasource.yaml # Grafana Data Source config
├── grafana-dashboard-provider.yaml# Grafana Dashboard config
├── grafana-service.yaml # Grafana NodePort Service
├── k8s-dashboard.json # Grafana Dashboard JSON
├── prometheus-nodeport.yaml # Prometheus NodePort Service
├── .github/workflows/docker-ci.yml# CI/CD pipeline


---

## ⚡ Setup Instructions

1️⃣ Clone Repository 

git clone https://github.com/shipravashist/devsecops-demo.git
cd <your-repo>

2️⃣ Build & Push Docker Image
docker build -t shipravashist/devsecops-demo:v1 .
docker push shipravashist/devsecops-demo:v1

3️⃣ Deploy on Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f networkpolicy.yaml

4️⃣ Install Prometheus & Grafana (via Helm)
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

helm install prometheus prometheus-community/prometheus
helm install grafana grafana/grafana

5️⃣ Expose Services
kubectl apply -f prometheus-nodeport.yaml
kubectl apply -f grafana-service.yaml


Prometheus → http://localhost:<nodeport>
Grafana → http://localhost:<nodeport>

Default Grafana credentials:
User: admin
Password: Retrieved from Kubernetes secret.



📊 Dashboards
Pre-configured Grafana dashboards available in k8s-dashboard.json.
Monitor app metrics, cluster health, and security posture.


🔐 Security Highlights
Pods run as non-root with restricted permissions.
Network Policies to control traffic.
Trivy Scans integrated into CI/CD.


📌 Future Improvements
Add SonarQube for code quality.
Integrate OWASP Dependency-Check.
Automate dashboard provisioning with Helm.
