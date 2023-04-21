import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

pickle.load(open('/home/fazilk/Documents/PW_Assignments/forestfire-main/models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('/home/fazilk/Documents/PW_Assignments/forestfire-main/models/ridge.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__=='main':
    app.run(host="0.0.0.0")