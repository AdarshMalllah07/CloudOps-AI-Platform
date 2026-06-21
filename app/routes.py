from flask import render_template
from services.incident_analyzer import analyze_incident

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

     analysis = analyze_incident(
        cpu_usage=85,
        memory_usage=72,
        disk_usage=60
    )

     return render_template(
        "ai/assistant.html",
        analysis=analysis
    )