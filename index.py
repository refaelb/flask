
import os
from os import name
from flask import render_template
from test import test


from flask import Flask
app = Flask(__name__)

def test(name):
    os.system('mkdir '+name)

@app.route('/', methods=['GET', 'POST'])
def home():
   return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    name = request.form['userValue']
    # name = 're'
    # return render_template('log.html')
    test(name)
      