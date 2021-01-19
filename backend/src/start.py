import bcrypt
from sanic import app
from sanic.exceptions import abort
from sanic.request import Request
from sanic_auth import Auth
from sanic_restplus.restplus import restplus
from spf import SanicPluginsFramework
from sanic_session import Session, InMemorySessionInterface
from .config import PORT
from .api import api
from .api.resources import *

app = app.Sanic("Flowtr Panel Backend")
spf = SanicPluginsFramework(app)
rest_assoc = spf.register_plugin(restplus)
session = Session(app, interface=InMemorySessionInterface())
auth = Auth(app)

rest_assoc.api(api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, workers=2)
