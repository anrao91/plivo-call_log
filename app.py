from pprint import pprint
import os
from flask import Flask, request, render_template
import requests
app = Flask(__name__) 

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/makeCall/", methods=['GET', 'POST'])
def makeCall():
    response = requests.get('https://api.plivo.com/v1/Account/MANTK5MTRIOTLIYZC2MT/Call/?status=live',auth = requests.auth.HTTPBasicAuth('MANTK5MTRIOTLIYZC2MT','ODI5Y2I0ZGYzODJhNWY4ZGQ4MjU0ODYxZDYxOTdj'))
    data = response.json()
    call_log = " ".join(data['calls']) 
    call_log = call_log + "Hello"
    return render_template('makeCall.html',call_log = call_log) # do something

@app.route("/listCall/", methods=['GET', 'POST'])
def listCall():
    return render_template('listCall.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
