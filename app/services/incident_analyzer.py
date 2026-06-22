def analyze_incident(cpu_usage, memory_usage, disk_usage):

    severity = "LOW"

    issues = []
    recommendations = []
    recovery_actions = []

    if cpu_usage > 80:

        severity = "HIGH"

        issues.append("High CPU Utilization")

        recommendations.append(
            "Traffic surge or application bottleneck detected."
        )

        recovery_actions.append(
            "Scale Kubernetes deployment."
        )

    if memory_usage > 80:

        severity = "HIGH"

        issues.append("High Memory Utilization")

        recommendations.append(
            "Possible memory leak detected."
        )

        recovery_actions.append(
            "Restart deployment and inspect memory usage."
        )

    if disk_usage > 85:

        if severity != "HIGH":
            severity = "MEDIUM"

        issues.append("Disk Space Running Low")

        recommendations.append(
            "Logs or temporary files consuming storage."
        )

        recovery_actions.append(
            "Clean logs and increase storage capacity."
        )

    if not issues:

        issues.append("System Healthy")

        recommendations.append(
            "No action required."
        )

        recovery_actions.append(
            "Monitoring only."
        )

    return {
        "severity": severity,
        "issues": issues,
        "recommendations": recommendations,
        "recovery_actions": recovery_actions
    }