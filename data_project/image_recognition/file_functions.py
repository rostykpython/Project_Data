from PIL import Image
import tensorflow as tf
import numpy as np


def open_file_handler(path_to_img, model):
    img = Image.open(path_to_img)
    img_array = tf.keras.utils.img_to_array(img)
    # if img_array.shape != (32, 32, 3):
    #     img_array = tf.image.resize(img_array, (32, 32))

    preprocessed_img_array = np.stack((img_array, ), axis=0)

    class_number = np.argmax(model.predict(preprocessed_img_array))
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    return class_names[class_number]



