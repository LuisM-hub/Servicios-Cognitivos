from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests
from pprint import pprint
import os 

subscription_key = "5ab33de5de3547018719d08cb0fc0d51" 
endpoint = "https://encuestas.cognitiveservices.azure.com/"
language_api_url = endpoint + "/text/analytics/v3.0/languages"

app = Flask(__name__)

from azure import documents

@app.route('/')
def inicio():
    return render_template("codigo.html")

@app.route('/json')
def json():
    print("EUREKA")
    return jsonify(documents)