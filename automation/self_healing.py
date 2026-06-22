from app.services.prometheus_service import get_system_metrics
from app.services.incident_analyzer import analyze_incident

from recovery_actions import (
    restart_deployment,
    scale_deployment
)


def run():

    metrics = get_system_metrics()

    print("Metrics:")
    print(metrics)

    analysis = analyze_incident(
        cpu_usage=metrics["cpu"],
        memory_usage=metrics["memory"],
        disk_usage=metrics["disk"]
    )

    print("\nAnalysis:")
    print(analysis)

    if metrics["cpu"] > 80:

        print("\nACTION: Scaling deployment")

        scale_deployment(5)

    if metrics["memory"] > 90:

        print("\nACTION: Restarting deployment")

        restart_deployment()


if __name__ == "__main__":
    run()