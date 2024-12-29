from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    year = datetime.now().year

    return render_template('index.html', year=year)