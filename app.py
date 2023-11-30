from flask import Flask, render_template, request,redirect,url_for,json,make_response,jsonify
import pandas as pd
import requests
import json
import numpy as np
from sklearn.cluster import KMeans
from rtree import index
from knn_search import find_nearest_neighbors

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/knn',methods=['POST'])
def knn():
    data = request.json
    key_value = data['key']
    print(key_value)
    response_data = find_nearest_neighbors(key_value, 5)
    return jsonify(response_data)


if __name__ == '__main__':
    app.run()  # Ejecuta la aplicación en modo de depuración
