#-*- coding:utf-8 -*-

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment 
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app=Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['SECRET_KEY'] = 'hard to guess string'

'''
@app.route('/datetime')
def show_datetime():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/test/<name>')
def test(name):
    return render_template('test.html', name=name)
'''

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


'''
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

'''

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('submit')

if __name__ == '__main__':
    app.run(debug=True)