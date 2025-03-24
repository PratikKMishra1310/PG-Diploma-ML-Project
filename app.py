import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/') #index or landing page of website
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST']) #post method is used to send parameters in http request
def predict():
    '''
    For rendering results on HTML GUI'''
    features = [x for x in request.form.values()]
    print("Features are ", features, " No of features =", len(features))
    prediction = model.predict(features)
    return render_template('index.html', 
    	prediction_text='Predicted type of accident is {}'
        .format(prediction))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9000) # EC2 on AWS