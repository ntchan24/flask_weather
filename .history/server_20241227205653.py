from flask import Flask, render_template, request
from weather import get_current_weather

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'helloworld'