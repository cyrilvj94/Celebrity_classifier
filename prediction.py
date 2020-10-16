from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import numpy as np

class CelebPrediction:
    """
    Contains all functions necessary for predicting the image
    :param : filename of the image to be predicted
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def predict(self):
        model  = load_model('model.h5')
        image = load_img(self.file_name, target_size=(256, 256))
        image = img_to_array(image)
        image = np.array([image])
        prediction = model.predict_classes(image)[0]
        class_labels = {0:'christiano ronaldo', 1:'de bruyne', 2:'leo messi', 3:'salah'}
        return [{"image":class_labels[prediction]}]



