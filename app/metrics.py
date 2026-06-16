from prometheus_client import Counter

request_counter = Counter(
    "cloudops_requests_total",
    "Total requests received"
)