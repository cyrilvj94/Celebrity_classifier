from flask import Flask, render_template, url_for, jsonify, request
from train_model import CNN_model
from flask_cors import CORS, cross_origin
import os
from utils.utils import decodeImage
from prediction import  CelebPrediction

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = CelebPrediction(self.filename)

@app.route('/', methods = ['GET'])
@cross_origin()
def homepage():
    return  render_template('index.html')

@app.route('/retrain')
@cross_origin()
def retrain():
    model_train = CNN_model()
    train_data = model_train.obtain_data('Dataset/Train_set', (256,256), 32)
    test_data = model_train.obtain_data('Dataset/Test_set', (256, 256), 32)
    new_model = model_train.create_model()
    new_model = model_train.compile_train(new_model, train_data, test_data, epochs = 6)
    new_model.save('model_retrained.h5')

@app.route('/predict', methods = ['POST'])
@cross_origin()
def predict():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)

if __name__=='__main__':
    clApp = ClientApp()
    app.run(host = 'localhost', port = 8000,debug = True)