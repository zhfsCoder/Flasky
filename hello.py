#-*- coding:utf-8 -*-

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment 
from datetime import datetime

app=Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

mydict = {'key':123, 'hha':'231'}

@app.route('/datetime')
def show_datetime():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/test/<name>')
def test(name):
    return render_template('test.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reuser/<name>')
def reuser(name):
    return render_template('user.html', name=name)

@app.route('/user_agent')
def agent():
    user_agent = request.headers.get('User_Agent')
    return '<h1>Hello world</h1> </br> <p>Your browser is %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return 'Hello %s' % name

if __name__ == '__main__':
    app.run(debug=True)