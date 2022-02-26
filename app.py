from unittest import result
from flask import Flask, render_template, redirect, url_for, request, current_app
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():

    data = []
    data2 = []
    if request.method == 'POST':
        print("Post Call")
        if request.form.get('pred') == 'Predict':
            print("Prediction")
            model = pickle.load(current_app.open_resource('model.pkl'))
            scaler = pickle.load(current_app.open_resource('scaler.pkl'))
            print(model)
            work_class = request.form.get('work_class')
            education = request.form.get('education')
            marital_status = request.form.get('marital_status')
            occupation = request.form.get('occupation')
            relationship = request.form.get('relationship')
            race = request.form.get('race')
            sex = request.form.get('sex')
            data=[[int(work_class),int(education),int(marital_status),int(occupation),int(relationship),int(race),int(sex)]]
            data2=scaler.transform(data)
            print(data2)
            prediction=model.predict(data2)
            if(prediction[0] == 0):
                final = '<=50K'
            else:
                final = '>50K'
            return render_template('predict.html', prediction=final)
        if request.form.get('back') == 'Back':
            print("Prediction")
            return redirect(url_for('index'))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
