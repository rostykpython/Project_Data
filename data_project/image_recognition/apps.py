from django.apps import AppConfig
from keras.models import load_model


class ImageRecognitionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_recognition'

    MODEL_PATH_EFFNET = './static/models_nn/eff_model_(0.9186).h5'

    pretrained_model_effnet = load_model(MODEL_PATH_EFFNET)
    pretrained_model_effv2 = load_model('./static/models_nn/model_effv2')
    pretrained_model_xception = load_model('./static/models_nn/asadadad-20220708T185154Z-001')

