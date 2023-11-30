from flask import Flask, render_template, jsonify, request
import flask_cors
import pandas as pd
import json
import numpy as np
from sklearn.cluster import KMeans
from rtree import index
from knn_search import find_nearest_neighbors

app = Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/knn',methods=['POST'])
def knn():
    key_value = request.form.get('key')
    method = request.form.get('method')
    match method:
        case 'knn':
            response_data = find_nearest_neighbors(key_value, 5)
        case 'pca':
            # response_data = lo que hace la funcion con pca
            pass
        case 'rtree':
            pass

    #response_data = [['id1','song1','author1','distance1'],['id2','song2','author2','distance2'],['id3','song3','author3','distance3'],['id4','song4','author4','distance4'],['id5','song5','author5','distance5']]
    # retornar con formato lista de listas
    return jsonify(response_data)


if __name__ == '__main__':
    app.run()  # Ejecuta la aplicación en modo de depuración
