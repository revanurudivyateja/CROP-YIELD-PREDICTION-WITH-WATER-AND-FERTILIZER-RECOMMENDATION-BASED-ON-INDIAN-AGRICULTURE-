from flask import Flask, render_template, request, Markup
import pickle
import numpy as np
import requests
model=pickle.load(open('models/model.pkl', 'rb'))

app = Flask(__name__)
@ app.route('/')
def home():
    title = 'MyCrop - Home'
    return render_template('index.html', title=title)

@ app.route('/crop-recommend')
def crop_recommend():
    title = 'MyCrop - Crop Recommendation'
    return render_template('Crop_result.html', title=title)


@app.route('/predict', methods=['POST'])
def predict():
#    print(request.form)
    int_features = [float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict(final)
#    output='{0:.{1}f}'.format(prediction[0][1], 2)
    return render_template('Crop_recommend.html', pred="Reccommended crop is : {}".format(prediction))

if __name__ == '__main__':
    app.run(debug=True)