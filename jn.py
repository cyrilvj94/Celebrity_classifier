import tensorflow as tf
print(tf.__version__)

#from tensorflow.keras.models import load_model


new_model = tf.keras.models.load_model('model.h5')