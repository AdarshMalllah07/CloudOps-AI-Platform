from flask import render_template


def register_routes(app):

    @app.route("/")
    def dashboard():
        return render_template(
            "infrastructure/dashboard.html"
        )