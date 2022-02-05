#!/usr/bin/env python
# encoding: utf-8

import json
from multiprocessing import context
import os
from requests import request
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])

def def_root():
    return "ddx manager api"


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5050, ssl_context=('/flaskapp/certs/cert.pem', '/flaskapp/certs/key.pem'), debug=True)

