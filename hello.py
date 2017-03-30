#-*- coding:utf-8 -*-

from flask import Flask, request, render_template

app=Flask(__name__)

mydict = {'key':123, 'hha':'231'}

@app.route('/test')
def test():
    return render_template('test.html')

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