from flask import Flask
from flaskwebgui import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app)

import front_end.urls