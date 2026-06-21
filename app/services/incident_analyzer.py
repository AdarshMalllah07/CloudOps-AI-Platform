def analyze_incident(cpu_usage, memory_usage, disk_usage):
    severity = "LOW"
    issues = []
    recommendations = []

    if cpu_usage > 80:
        severity = "HIGH"
        issues.append("High CPU Utilization")
        recommendations.append(
            "Investigate running processes and consider scaling."
        )

    if memory_usage > 80:
        severity = "HIGH"
        issues.append("High Memory Utilization")
        recommendations.append(
            "Check memory leaks and optimize applications."
        )

    if disk_usage > 85:
        severity = "MEDIUM"
        issues.append("Disk Space Running Low")
        recommendations.append(
            "Clean logs and increase storage capacity."
        )

    if not issues:
        issues.append("System Healthy")
        recommendations.append(
            "No action required."
        )

    return {
        "severity": severity,
        "issues": issues,
        "recommendations": recommendations
    }