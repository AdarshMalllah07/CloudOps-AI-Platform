from flask import render_template
from services.incident_analyzer import analyze_incident
from services.prometheus_service import get_system_metrics
from metrics import request_counter

from environment_repository import get_all_environments
from server_repository import get_all_servers
from application_repository import get_all_applications


def register_routes(app):

    @app.route("/")
    def dashboard():

        request_counter.inc()

        return render_template(
            "dashboard/dashboard.html"
        )

    @app.route("/infrastructure")
    def infrastructure():

        request_counter.inc()

        environments = get_all_environments()
        servers = get_all_servers()
        applications = get_all_applications()

        return render_template(
            "infrastructure/infrastructure.html",
            environments=environments,
            servers=servers,
            applications=applications
        )

    @app.route("/monitoring")
    def monitoring():

        request_counter.inc()

        return render_template(
            "monitoring/monitoring.html"
        )

    @app.route("/cost-optimization")
    def cost_optimization():

        request_counter.inc()

        return render_template(
            "cost/cost.html"
        )

    @app.route("/ai-assistant")
    def ai_assistant():

        request_counter.inc()

        metrics = get_system_metrics()

        analysis = analyze_incident(
            cpu_usage=metrics["cpu"],
            memory_usage=metrics["memory"],
            disk_usage=metrics["disk"]
        )

        return render_template(
            "ai/assistant.html",
            analysis=analysis,
            metrics=metrics
        )
    
    @app.route("/ai-operations")
    def ai_operations():

    metrics = get_system_metrics()

    analysis = analyze_incident(
        cpu_usage=metrics["cpu"],
        memory_usage=metrics["memory"],
        disk_usage=metrics["disk"]
    )

    return render_template(
        "ai/operations.html",
        metrics=metrics,
        analysis=analysis
    )   