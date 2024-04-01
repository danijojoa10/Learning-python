from flask import Flask, render_template, jspnify
import request 

app = Flask (__name__)
url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"
api_key_nasa='fXooYfQkn5SXaGb28bNAiL5vIcdf6Tz5Ni7mUmYH'

app.route('/')

def index():
    params = {
        'api key'= api_key_nasa
    }

response = requests. get(url, params=params)
if response.status_code == 200:
    data = response.json()

    return render_template('index.html',data = data)

else: f"error"(response.status_code)


