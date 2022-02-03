import os
from os import path

from flask import Flask
from flask import render_template


app = Flask(__name__)

app.secret_key = 'apdsifjgr'


@app.route("/")
def index():
    return render_template('index.html')