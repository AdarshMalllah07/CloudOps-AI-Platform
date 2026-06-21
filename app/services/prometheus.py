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

    cpu = get_metric("100 - (avg by(instance)(rate(node_cpu_seconds_total{mode='idle'}[5m])) * 100)")

    memory = get_metric(
        "(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100"
    )

    disk = get_metric(
        "(1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)) * 100"
    )

    return {
        "cpu": round(cpu, 2),
        "memory": round(memory, 2),
        "disk": round(disk, 2)
    }