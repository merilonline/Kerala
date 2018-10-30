from flask import Flask
from flask_ask import Ask,question,statement,session
import random

app = Flask(__name__)
ask = Ask(app, '/')


@app.route("/hello")
def hello():
    return "Hello World!"

@ask.launch
def start_skill():
    welcome_message = 'Hello'
    return statement(welcome_message)

@ask.intent('GetNewFactIntent')
def intent():
    foo = ['Thiruvalla is a beautiful city', 'Thiruvalla is a very developed city', 'Thiruvalla is good', 'Thiruvalla is very calm','Thiruvalla is a peaceful city']
    text = 'Hello, '+random.choice(foo)
    return statement(text)
