from flask import Flask, render_template, request
import requests
import pickle
import logging

import sys


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
       # vendor = float(request.form['vendor'])
        myct=float(request.form['myct'])
        mmin=float(request.form['mmin'])
        mmax=float(request.form['mmax'])
        cach=float(request.form['cach'])
        chmin=float(request.form['chmin'])
        chmax=float(request.form['chmax'])

        prediction=model.predict([[myct, mmin, mmax, cach, chmin, chmax]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_text="Sorry you cannot predict this performance")
        else:
            return render_template('index.html',prediction_text="Your model performance is {} ".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

