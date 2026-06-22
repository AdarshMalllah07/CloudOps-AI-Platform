from flask import Flask, request, jsonify

from recovery_actions import (
    restart_deployment,
    scale_deployment
)

app = Flask(__name__)


@app.route("/webhook/alert", methods=["POST"])
def alert():

    data = request.json

    print("Webhook received")
    print(data)

    alerts = data.get("alerts", [])

    for alert in alerts:

        alert_name = alert["labels"].get("alertname")

        print(f"Alert Received: {alert_name}")

        if alert_name == "HighCPUUsage":

            print("Scaling deployment to 5 replicas")

            scale_deployment(5)

        if alert_name == "PodRestartDetected":

            print("Restarting deployment")

            restart_deployment()

    return jsonify({
        "status": "success"
    })


@app.route("/")
def home():
    return "Alert Listener Running"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5050
    )