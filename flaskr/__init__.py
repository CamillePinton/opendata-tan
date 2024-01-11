from flask import Flask, request, render_template
import os
import requests
from flask_swagger_ui import get_swaggerui_blueprint

"""
to run the app, do
flask --app flaskr run
or in pycharm:
-edit configuration
-set Target type to 'Module name'
-set Target to 'flaskr'
"""

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "opendata-tan"
    }
)

def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(swaggerui_blueprint)

    opendata_link = "https://open.tan.fr"

    if test_config:
        app.config.update({
            "TESTING": True,
        })

    @app.route('/')
    def hello_world():
        return render_template('index.html')


    # Recherche arrets proche d'une latitude/longitude
    @app.route('/find_arret/<latitude>/<longitude>', methods=['GET'])
    def get_closest_arret(latitude, longitude):
        return requests.get(opendata_link + f"/ewp/arrets.json/{latitude}/{longitude}").json()


    # Liste de tous les arrets
    @app.route('/arrets', methods=['GET','POST'])
    def get_arrets_by_ligne():
        arrets = requests.get(opendata_link + '/ewp/arrets.json').json()
        if request.method == 'POST':
            # Retrieve the text from the textarea
            num_ligne = request.form.get('textarea').replace('\n','').replace(' ','')
            # Print the text in terminal for verification
            arrets_ligne = []
            for arret in arrets:
                if {"numLigne": num_ligne} in arret['ligne']:
                    arrets_ligne.append(arret)
            return render_template('arrets.jinja2', arrets=arrets_ligne)
        return render_template('arrets.jinja2', arrets=arrets)


    # Horaires (théoriques)
    @app.route('/horaires/<codeArret>/<numLigne>/<sens>', methods=['GET'])
    def get_horaires(codeArret, numLigne, sens):
        return requests.get(opendata_link + f"/ewp/horairesarret.json/{codeArret}/{numLigne}/{sens}").json()

    # Temps Attente
    @app.route('/tempsattente/<codeArret>', methods=['GET'])
    def get_temps_attente(codeArret):
        return requests.get(opendata_link + f"/ewp/tempsattente.json/{codeArret}").json()

    # Temps attente pour un lieu ou arret et un nombre de passages
    @app.route('/tempsattente/<codeArret>/<nbPassages>', methods=['GET'])
    def get_temps_attente_pour_lieu_ou_arret_et_nbPassages(codeArret, nbPassages):
        return requests.get(opendata_link + f"/ewp/tempsattentelieu.json/{codeArret}/{nbPassages}").json()

    # Temps attente pour un lieu ou arret, un nombre de passages et un numéro de ligne
    @app.route('/tempsattente/<codeArret>/<nbPassages>/<numLigne>', methods=['GET'])
    def get_temps_attente_pour_lieu_ou_arret_et_nbPassages_et_numLigne(codeArret, nbPassages, numLigne):
        return requests.get(opendata_link + f"/ewp/tempsattentelieu.json/{codeArret}/{nbPassages}/{numLigne}").json()
    
    
    return app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host='0.0.0.0', port=port)