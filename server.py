# -*- coding: utf-8 -*- 
from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template

app = Flask(__name__)

def get_menu():
    return [
        {"header":u"о компании","child":[],'disabled':1,},
        {"header":u"вход в систему","url":'/login'},
        {"header":u"о главная",'act':1},
        {
            "header":u"каталог",
            "child":[
                {"header":u"велосипеды"},
                {"header":u"мотоциклы"},
            ]
        },
        {"header":u"контакты"}
    ]

def get_promo():
    return {
        "title":"title",
        "description":"description",
        "keywords":"keywords"
    }

promo=get_promo()
menu=get_menu()


@app.route('/')
def index():
    #response = make_response('<h1>response!</h1>')
    #response.set_cookie('answer','42')
    #return response
    user = {'username': 'Miguel'}
    
    return render_template('main.html',
        promo=promo,
        content={
            "header":u'Добро пожаловать',
            "body":u'съешь этих мягких французских булок, да выпей чаю'
        },
        menu=menu,
        flag=1
    )


@app.route('/login')
def login_form():
    return render_template('login_form.html',
        promo=promo,
        content={
            "header":u'вход в систему',
            "body":u'в этой форме мы входим в систему'
        },
    )

@app.route('/302')
def redirect1():
    return redirect('/',302)

@app.route('/301')
def redirect2():
    #return '301'
    return redirect('/',301)


if __name__=='__main__':
    app.run(port=7000, debug=True)