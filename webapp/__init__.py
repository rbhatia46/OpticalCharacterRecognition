from flask import Flask, render_template

from webapp.blueprints.api import api


app = Flask(__name__, static_url_path='', static_folder='statics')
app.register_blueprint(api)

@app.route("/")
def hello():
    return render_template('home.html')
