from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Setup Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "Hello DevSecOps 🚀"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
