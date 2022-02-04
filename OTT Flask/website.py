from distutils.log import debug
from flask import Flask, render_template, request
import numpy as np
import pickle
import os

website = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

picFolder = os.path.join('static','pics')
website.config['UPLOAD_FOLDER'] = picFolder

@website.route("/")
def hello_world():
    logo1 = os.path.join(website.config['UPLOAD_FOLDER'], 'netflixlogo.jpeg')
    logo2 = os.path.join(website.config['UPLOAD_FOLDER'], 'disneylogo.jpeg')
    logo3 = os.path.join(website.config['UPLOAD_FOLDER'], 'amazonlogo.jpeg')
    return render_template('index.html', netlogo = logo1, dislogo = logo2, amazlogo = logo3)

@website.route("/recommender", methods=['GET'])
def recommender():
    return render_template('recommender.html')

@website.route("/predict", methods=['POST'])
def predict():
    type = request.form.get('type')
    age = request.form.get('age')
    genre = request.form.get('genre')
    language = request.form.get('language')
    imdb = request.form.get('imdb')
    features = [genre,language,type,age,imdb]
    final_features = [float(ele) for ele in features]
    final_features1 = np.reshape(final_features, (1, 5))
    prediction = model.predict(final_features1)
    print(prediction)
    if(prediction[0] == 1):
        logo1 = os.path.join(website.config['UPLOAD_FOLDER'], 'netflixlogo.jpeg')
        return render_template('netflix_predict.html', netlogo = logo1)
    elif(prediction[0] == 2):
        logo2 = os.path.join(website.config['UPLOAD_FOLDER'], 'disneylogo.jpeg')
        return render_template('disney_predict.html', dislogo = logo2)
    else:
        logo3 = os.path.join(website.config['UPLOAD_FOLDER'], 'amazonlogo.jpeg')
        return render_template('amazon_predict.html', amazlogo = logo3)

@website.route("/netflix")
def netflix():
    pic1 = os.path.join(website.config['UPLOAD_FOLDER'], 'netflixtype.jpeg')
    pic2 = os.path.join(website.config['UPLOAD_FOLDER'], 'netflixtypepie.jpeg')
    pic3 = os.path.join(website.config['UPLOAD_FOLDER'], 'netflixage.jpeg')
    pic4 = os.path.join(website.config['UPLOAD_FOLDER'], 'netflixagepie.jpeg')
    return render_template('netflix.html', nettype = pic1, nettypepie = pic2, netage = pic3, netagepie = pic4)

@website.route("/disney")
def disney():
    pic5 = os.path.join(website.config['UPLOAD_FOLDER'], 'disneytype.jpeg')
    pic6 = os.path.join(website.config['UPLOAD_FOLDER'], 'disneytypepie.jpeg')
    pic7 = os.path.join(website.config['UPLOAD_FOLDER'], 'disneyage.jpeg')
    pic8 = os.path.join(website.config['UPLOAD_FOLDER'], 'disneyagepie.jpeg')
    return render_template('disney.html', distype = pic5, distypepie = pic6, disage = pic7, disagepie = pic8)

@website.route("/amazon")
def amazon():
    pic9 = os.path.join(website.config['UPLOAD_FOLDER'], 'amazontype.jpeg')
    pic10 = os.path.join(website.config['UPLOAD_FOLDER'], 'amazontypepie.jpeg')
    pic11 = os.path.join(website.config['UPLOAD_FOLDER'], 'amazonage.jpeg')
    pic12 = os.path.join(website.config['UPLOAD_FOLDER'], 'amazonagepie.jpeg')
    return render_template('amazon.html', amaztype = pic9, amaztypepie = pic10, amazage = pic11, amazagepie = pic12)

@website.route("/netflix_predict")
def netflix_predict():
    return render_template('netflix_predict')

@website.route("/disney_predict")
def disney_predict():
    return render_template('disney_predict')

@website.route("/amazon_predict")
def amazon_predict():
    return render_template('amazon_predict')

if __name__ == "__main__":
    website.run(debug=True)