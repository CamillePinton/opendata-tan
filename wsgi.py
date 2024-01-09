from flask import Flask
import requests

app = Flask(__name__)

opendata_link = "https://open.tan.fr"


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Recherche arrets proche d'une latitude/longitude
@app.route('find_arret/<latitude>/<longitude>')
def get_closest_arret(latitude, longitude):
    req = requests.get(opendata_link + "/ewp/arrets.json/{latitude}/{longitude}")
    return req


# Liste de tous les arrets
@app.route('/arrets', methods=['GET'])
def get_arrets():
    arrets = requests.get(opendata_link + '/ewp/arrets.json').json()
    return arrets

# Horaires (théoriques)

# Temps Attente

# Temps attente pour un lieu ou arret et un nombre de passages

# Temps attente pour un lieu ou arret, un nombre de passages et un numéro de ligne
