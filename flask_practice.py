from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello, World'
    return app.root_path

@app.route('/upper')
def uppercase():
    return render_template("html_practice.html")

@app.route('/upper', methods=['POST'])
def uppercase_post():

    text = request.form['text']
    processed_text = text.upper()
    return processed_text