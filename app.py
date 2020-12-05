from flask import Flask, render_template, request, redirect, url_for, session, flash
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression

# create instance of the flask
app = Flask(__name__)
app.secret_key == "hello"


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        int_features = [x for x in request.form.values()]
        print(int_features)
        final_features = [np.array(int_features)]
        prediction = model_predict(final_features)
        prediction = prediction[0]
        print(prediction)
        if prediction == "unacc":
            prediction =  "Unacceptable"
        elif prediction == "acc":
            prediction =  "Acceptable"
        elif prediction == "good":
            prediction =  "Good"
        elif prediction == "vgood":
            prediction =  "Very Good"
        return render_template("car.html", prediction_text='Car condition is {}'.format(prediction))
    else:
        return render_template("car.html")

def model_predict(final_features):
    loaded_model = pickle.load(
        open(r"H:\workspace\flask_resources\github_projects\car_evaluation\svm_model.pkl", 'rb'))
    print(loaded_model.predict(final_features))
    return loaded_model.predict(final_features)


if __name__ == "__main__":
    app.secret_key = 'easy'
    app.run(debug=True)
