from flask import Flask, render_template, request
from weather import get_current_weather

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'helloworld'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000) #localhost port 8000
    