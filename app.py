# Here's what the code is doing:
# 1.It loads the index.html file and returns it to the browser
# 2. It returns a string that is the JSON representation of the JSON object
# 3. It returns a random item from the JSON list
# 4. It returns the JSON data of the API number you input

# pdoc3 was used to generate the documentation

# Imports
from flask import Flask, render_template
import json
import random
from rich import *

# Creating a Flask object.
app = Flask(__name__)


#* source for data is https://github.com/itmmckernan/triviaJSON and formatted by me
# Opening the data.json file and loading it into the JSON variable.
with open("data.json",encoding="utf8") as file:
    JSON = json.load(file)


@app.route('/')
def hmm():
    """
    It loads the index.html file and returns it to the browser
    :return: The index.html file is being returned.
    """
    
    #load the index.html file
    return render_template('main.html')


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
    num = random.randint(0,206)
    return JSON[num]


@app.route('/api/<int:Number>')
def apis(Number):
    """
    It returns the JSON data of the API number you input
    
    :param Number: The number of the API you want to use
    :return: The JSON data
    """
    return JSON[Number]

# Running the app.
if __name__ == '__main__':
    app.run()