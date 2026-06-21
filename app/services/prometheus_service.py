import requests

PROMETHEUS_URL = "http://cloudops-prometheus:9090"

def get_metric(query):
    try:
        response = requests.get(
            f"{PROMETHEUS_URL}/api/v1/query",
            params={"query": query},
            timeout=5
        )

        data = response.json()
        result = data.get("data", {}).get("result", [])

        if result:
            return float(result[0]["value"][1])

        return 0

    except Exception as e:
        print(f"Prometheus error: {e}")
        return 0


def get_system_metrics():
    return {
        "cpu": get_metric("up"),
        "memory": 0,
        "disk": 0
    }