
import os
from os import name
from flask import render_template
from werkzeug.datastructures import RequestCacheControl
# from werkzeug.datastructures import RequestCacheControl
from run import test
from flask import request



from flask import Flask
app = Flask(__name__)

def test(name):
    os.system('mkdir '+name)

@app.route('/' , methods=['GET','POST'])
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    namespace = request.form['namespace']
    chart = request.form['chart']
    host = request.form['host']
    repo = request.form['repo']
    tag = request.form['tag']
    reg = request.form['reg']
    branch = request.form['branch']
    homedir = request.form['homedir']


    test(namespace)
    return render_template('log.html')

    