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
    foo = ['Kerala is a state on the southwestern, Malabar Coast of India','Kerala is spread over 38,863 square km','Kerala is divided into 14 districts with the capital being Thiruvananthapuram','Malayalam is the most widely spoken language ','The Chera Dynasty was the first prominent kingdom based in Kerala','it is bordered by Karnataka to the north and northeast, Tamil Nadu to the east and south, and the Lakshadweep Sea to the west']
    text = 'Hello, '+random.choice(foo)
    return statement(text)
