from flask import render_template


def register_routes(app):

    @app.route("/")
    def dashboard():
        return render_template("dashboard/dashboard.html")

    @app.route("/infrastructure")
    def infrastructure():
        return render_template("infrastructure/infrastructure.html")

    @app.route("/monitoring")
    def monitoring():
        return render_template("monitoring/monitoring.html")

    @app.route("/cost-optimization")
    def cost_optimization():
        return render_template("cost/cost.html")

    @app.route("/ai-assistant")
    def ai_assistant():
        return render_template("ai/assistant.html")