
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

Namespace='trutyru'
@app.route('/login', methods=['GET', 'POST'])
def login():
        
    # namespace = request.form['namespace']
    # chart = request.form['chart']
    # host = request.form['host']
    # repo = request.form['repo']
    # tag = request.form['tag']
    # reg = request.form['reg']
    # branch = request.form['branch']
    # homedir = request.form['homedir']

    # Namespace = namespace.upper()
    # Chart = chart.upper()
    # Host = host.upper()
    # Repo = repo.upper()
    # Tag = tag.upper()
    # Reg = reg.upper()
    # Branch = branch.upper()
    # Homedir = homedir.upper()

    test(Namespace)
    return render_template('log.html')

    


# @app.route('/login', methods=['GET', 'POST'])
# def login():
    
#     name = 'default_name'
#     # if request.method == 'POST' :
#     name = request.form['username']
#     os.system('mkdir '+name)
#     # else:


