from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask

from config import Config
from routes import register_routes

app = Flask(__name__)

app.config.from_object(Config)

register_routes(app)

app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,
    {
        "/metrics": make_wsgi_app()
    }
)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )