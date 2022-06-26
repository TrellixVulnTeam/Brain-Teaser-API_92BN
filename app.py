# pdoc3 was used to generate the documentation

# Imports
from flask import Flask, render_template
import json
import random
from rich import *

# Creating a Flask object.
app = Flask(__name__, template_folder='template')

#* source for data is https://github.com/itmmckernan/triviaJSON and formatted by me
# Opening the data.json file and loading it into the JSON variable.
with open("data.json", encoding="utf8") as file:
    JSON = json.load(file)


@app.route('/')
def Home():
    return render_template('app.html')


@app.route('/raw')
def raw():
    """
    It returns a string that is the JSON representation of the JSON object
    :return: A string
    """
    return json.dumps(JSON)


@app.route('/api')
def api():
    """
    It returns a random item from the JSON list
    :return: A random number between 0 and 206
    """
    num = random.randint(0, 206)
    return JSON[num]


@app.route('/api/<int:Number>')
def apis(Number):
    """
    It returns the JSON data of the API number you input
    
    :param Number: The number of the API you want to use
    :return: The JSON data
    """
    if Number > 206 and Number < 0:
        return "Error: Invalid API number"
    else:
        return JSON[Number]


# Running the app.
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
