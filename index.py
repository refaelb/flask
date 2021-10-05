
import os
from os import name
from flask import render_template
from werkzeug.datastructures import RequestCacheControl
# from werkzeug.datastructures import RequestCacheControl
from run import test
from flask import request



from flask import Flask
app = Flask(__name__)

# def test(name):
#     os.system('mkdir '+name)

@app.route('/', methods=['GET','POST'])
def home():
   return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    
    name = 'default_name'
    if request.method == 'POST' :
        name = request.form['userValue']
        os.system('mkdir '+name)
    else:
        os.system('mkdir no_work')


