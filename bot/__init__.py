from flask import Flask
from bot.core.controllers import core
from bot.auth.controllers import auth


app = Flask(__name__)

app.register_blueprint(core)
app.register_blueprint(auth)
