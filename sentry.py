import sentry_sdk
import os

from bottle import Bottle, Response
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://fa87cecb9be04f63a430cc5a63627490@sentry.io/4039165",
    integrations=[BottleIntegration()]
)

app = Bottle()


@app.route('/fail')
def error():
    raise RuntimeError

@app.route('/success')
def ok():
    Response.status = 200

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host="localhost", port=8080, debug=True)