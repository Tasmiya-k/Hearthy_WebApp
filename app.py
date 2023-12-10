# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'heart-disease-prediction-knn-model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
	return render_template('index.html')
    
@app.route('/lipid_test')
def lipid_test():
    return render_template('lipid_test.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        sex = request.form.get('sex')
        cp = request.form.get('cp')
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = request.form.get('fbs')
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = request.form.get('exang')
        oldpeak = float(request.form['oldpeak'])
        slope = request.form.get('slope')
        ca = int(request.form['ca'])
        thal = request.form.get('thal')
        
        data = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
        
@app.route('/g_map')
def g_map():
    return render_template('g_map.html')

@app.route('/ecg')
def ecg():
    return render_template('ecg.html')

@app.route('/videoCall')
def videoCall():
     return render_template('vid.html')

@app.route('/lifestyleSurvey')
def lifestyleSurvey():
     return render_template('lifestyle.html')

@app.route('/lifestyleResult', methods=['GET', 'POST'])
def lifestyleResult():
     if request.method == 'POST':
        # Fetch all form data
        form_data = {}
        for field in request.form:
            form_data[field] = request.form[field]

        # Pass form data to the result.html template
        return render_template('lifestyle_result.html', form_data=form_data)

if __name__ == '__main__':
	app.run(debug=True)

