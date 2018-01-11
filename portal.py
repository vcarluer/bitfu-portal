#!/usr/bin/python3
import subprocess
import logging
from flask import Flask, render_template, make_response, request, send_from_directory, abort

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    user = request.headers.get("X-User-Id")
    df = subprocess.Popen(["df", "-h", "/home/plexlib"], stdout=subprocess.PIPE)
    output = df.communicate()[0]
    strOutput = str( output, encoding='utf8' )
    logging.warning(strOutput)
    device, size, used, available, percent, mountpoint = \
                strOutput.split("\n")[1].split()
    return render_template('home.html', user=user, freeSpace=available)
