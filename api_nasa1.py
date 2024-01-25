'''
API: APPLICATION PROGGRAMING INTERFACE
NASA API: https://api.nasa.gov/
API-KEY-NASA: fXooYfQkn5SXaGb28bNAiL5vIcdf6Tz5Ni7mUmYH
DEVELOPER: DANILO JOJOA
DATE: 240124
SCRIPT-DESCRIPTION: OBTENER Y LEER DATOS DE LA NASA API DE COMETAS'''

import requests
import os

os.system('clear')

def get_comet_data(api_key):
    print(":::COMET INFORMATION:::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"
    
    try: 
        #realizar solicitud a la api
        response = requests.get(url)
        response.raise_for_status() #valida si presenta algun error en la peticion
        #convertir la respuesta a formato JSON (JS object notation)
        datos = response.json()

        print(f"commet name: {datos['name']}")
        print(f"magnitud absoluta: {datos['absolute_magnitude_h']}")
        print(f"diametro estimado maximo (KM) {datos['estimated_diameter']['kilometers']}")

    except requests.exceptions.RequestException as e: 
        print(f"error al realizar solicitud de informacion de la NASA: {e}")

api_key_nasa='fXooYfQkn5SXaGb28bNAiL5vIcdf6Tz5Ni7mUmYH'
get_comet_data(api_key_nasa)
