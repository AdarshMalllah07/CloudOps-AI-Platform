from services.prometheus_service import get_system_metrics

metrics = get_system_metrics()

print(metrics)