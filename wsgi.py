from flask import Flask
import requests
app = Flask(__name__)

open_tan="https://open.tan.fr"

@app.route('/')
def hello_world():
    return 'Hello, World!'

#Recherche arrets proche d'une latitude/longitude
@app.route('/<latitude>/<longitude>')
def getArret(latitude, longitude):
    req=requests.get(open_tan+"/ewp/arrets.json/{latitude}/{longitude}")
    return req
#Liste de tous les arrets

#Horaires (théoriques)

#Temps Attente

#Temps attente pour un lieu ou arret et un nombre de passages

#Temps attente pour un lieu ou arret, un nombre de passages et un numéro de ligne

