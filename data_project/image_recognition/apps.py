from django.apps import AppConfig
from tensorflow import keras


class ImageRecognitionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_recognition'

    MODEL_PATH = './static/models_nn/nn_test_dataproject.h5'
    pretrained_model = keras.models.load_model(MODEL_PATH)
