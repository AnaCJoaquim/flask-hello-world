# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/

from flask import Flask, render_template, request, url_for, flash, redirect 
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')

if (__name__) == "__main__":
   app.run(port="5100", debug="True") 