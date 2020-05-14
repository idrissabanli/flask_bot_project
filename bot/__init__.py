from flask import Flask
from bot.core.controllers import core


app = Flask(__name__)

app.register_blueprint(core)
