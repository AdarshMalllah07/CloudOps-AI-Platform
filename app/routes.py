from flask import render_template
from server_repository import get_all_servers
from application_repository import get_all_applications


def register_routes(app):

    @app.route("/")
    def dashboard():
        return render_template(
            "dashboard/dashboard.html"
        )

   @app.route("/infrastructure")
def infrastructure():

    environments = get_all_environments()
    servers = get_all_servers()
    applications = get_all_applications()

    return render_template(
        "infrastructure/infrastructure.html",
        environments=environments,
        servers=servers,
        applications=applications
    )
    )
    @app.route("/monitoring")
    def monitoring():
        return render_template("monitoring/monitoring.html")

    @app.route("/cost-optimization")
    def cost_optimization():
        return render_template("cost/cost.html")

    @app.route("/ai-assistant")
    def ai_assistant():
        return render_template("ai/assistant.html")