from django.apps import AppConfig
from keras.models import load_model


class ImageRecognitionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_recognition'

    pretrained_model_effv2 = load_model('./static/models_nn/model_effv2')
    pretrained_model_xception = load_model('./static/models_nn/model_xception')
    pretrained_model_vgg16 = load_model('./static/models_nn/model_vgg16')

