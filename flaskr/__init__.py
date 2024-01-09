from flask import Flask
import os
import requests
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

#-------------
SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={ 
        'app_name': "opendata-tan"
    }
)
app.register_blueprint(swaggerui_blueprint)
#-------------

opendata_link = "https://open.tan.fr"

# if test_config:
#     app.config.update({
#         "TESTING": True,
#     })

@app.route('/')
def hello_world():
    return 'Hello, World!'


# Recherche arrets proche d'une latitude/longitude
@app.route('/find_arret/<latitude>/<longitude>', methods=['GET'])
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


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # app = create_app()
    app.run(host='0.0.0.0', port=port)