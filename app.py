from flask import Flask, url_for, redirect, request, flash, abort
from flask import render_template, make_response
from flask import session, escape
from flask_mail import Mail, Message
import smtplib

app = Flask(__name__)

@app.route('/')
def hello():
    return 'HelloWorld'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')