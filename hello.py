#-*- coding:utf-8 -*-

from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/user/<name>')
def user(name):
    return 'Hello %s' % name

if __name__ == '__main__':
    app.run(debug=True)