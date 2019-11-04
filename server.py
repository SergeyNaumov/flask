# -*- coding: utf-8 -*- 
from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    #response = make_response('<h1>response!</h1>')
    #response.set_cookie('answer','42')
    #return response
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/302')
def redirect1():
    return redirect('/',302)

@app.route('/301')
def redirect2():
    #return '301'
    return redirect('/',301)


if __name__=='__main__':
    app.run(port=7000, debug=True)