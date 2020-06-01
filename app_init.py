from bot import app
import os

if __name__ == '__main__':
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.run(debug=True, port=5000)

from werkzeug.routing import RequestRedirect, MethodNotAllowed, NotFound
