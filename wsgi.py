from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/arrets', methods=['GET'])
def get_arrets():
    arrets = requests.get('https://open.tan.fr/ewp/arrets.json').json()
    return arrets
