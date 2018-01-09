#!/usr/bin/python3
import logging
from flask import Flask, render_template, make_response, request, send_from_directory, abort

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    user = request.headers.getlist("X-User-Id")
    return render_template('home.html', user=user)
