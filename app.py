#!/usr/bin/env python
"""This module contains the main application logic."""

from flask import Flask, request, render_template


APP = Flask(__name__, template_folder='templates')


@APP.route('/')
def home():
    '''
    Rendering Home Page
    '''
    return render_template('index.html')


@APP.route('/hello', methods=['POST'])
def hello():
    '''
    For rendering results on HTML GUI
    '''
    list(request.form.values())

    inputs = list(request.form.values())  # Adjusted line
    result = f"Hello There {inputs[0]}"  # Adjusted line
    return render_template('index.html', hello_text=result)  # Adjusted line


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080)
