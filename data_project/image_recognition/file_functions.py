from PIL import Image
import tensorflow as tf
import numpy as np
from .apps import ImageRecognitionConfig
from django.contrib import messages


def open_file_handler(path_to_img: str, model_name: str, request=None):

    class_names = ['airplane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog',
                   'horse', 'ship', 'truck']
    try:
        model, required_input_shape = get_pretrained_model(model_name)
        img = Image.open(path_to_img)
        img_array = tf.keras.utils.img_to_array(img)
        if img_array.shape != required_input_shape:
            img_array = tf.image.resize(img_array, (required_input_shape[0], required_input_shape[1]))
        preprocessed_img_array = np.stack((img_array, ), axis=0)
        class_number = np.argmax(model.predict(preprocessed_img_array))

    except (AttributeError, ValueError):
        return messages.error(request, message='You should check your input or the title of it!')

    predicted_value = class_names[class_number]
    return predicted_value


def get_pretrained_model(model_name):
    if model_name == 'EfficientNet':
        return ImageRecognitionConfig.pretrained_model_effnet, (80, 80, 3)
    elif model_name == 'EfficientNetV2':
        return ImageRecognitionConfig.pretrained_model_effv2, (32, 32, 3)
    elif model_name == 'Xception':
        return ImageRecognitionConfig.pretrained_model_xception, (32, 32, 3)


def get_class_information(class_name):

    info_dict = {
        'bird': 'Birds are a group of warm-blooded vertebrates constituting the class Aves, characterised '
                'by feathers, toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic rate, '
                'a four-chambered heart, and a strong yet lightweight skeleton. Birds live worldwide and range in '
                'size from the 5.5 cm (2.2 in) bee hummingbird to the 2.8 m (9 ft 2 in) ostrich. There are about ten '
                'thousand living species, more than half of which are passerine, or "perching" birds',
        'cat': 'The cat (Felis catus) is a domestic species of small carnivorous mammal. It is the only '
               'domesticated species in the family Felidae and is often referred to as the domestic cat to '
               'distinguish it from the wild members of the family. A cat can either be a house cat, a farm cat or '
               'a feral cat; the latter ranges freely and avoids human contact. Domestic cats are valued by humans '
               'for companionship and their ability to kill rodents. About 60 cat breeds are recognized by various '
               'cat registries',
        'car': 'A car (or automobile) is a wheeled motor vehicle that is used for transportation. Most definitions of '
               'cars say that they run primarily on roads, seat one to eight people, have four wheels, and mainly '
               'transport people instead of goods. The year 1886 is regarded as the birth year of the car when '
               'German inventor Carl Benz patented his Benz Patent-Motorwagen. Cars became widely available '
               'during the 20th century. One of the first cars affordable by the masses was the 1908 Model T, '
               'an American car manufactured by the Ford Motor Company',
        'deer': 'Deer or true deer are hoofed ruminant mammals forming the family Cervidae. The two main groups of '
                'deer are the Cervinae, including the muntjac, the elk (wapiti), the red deer, and the fallow deer; '
                'and the Capreolinae, including the reindeer (caribou), white-tailed deer, the roe deer, '
                'and the moose. Male deer of all species (except the water deer) as well as female reindeer, '
                'grow and shed new antlers each year',
        'dog': 'The dog or domestic dog (Canis familiaris or Canis lupus familiaris) is a domesticated '
               'descendant of the wolf, and is characterized by an upturning tail. The dog is derived from an '
               'ancient, extinct wolf, and the modern wolf is the dogs nearest living relative. The dog was '
               'the first species to be domesticated, by hunter–gatherers over 15,000 years ago, before the '
               'development of agriculture. Due to their long association with humans, dogs have expanded to a '
               'large number of domestic individuals and gained the ability to thrive on a starch-rich diet that '
               'would be inadequate for other canids',
        'frog': 'A frog is any member of a diverse and largely carnivorous group of short-bodied, tailless amphibians '
                'composing the order Anura (ανοὐρά, literally without tail in Ancient Greek). The oldest fossil '
                '"proto-frog" Triadobatrachus is known from the Early Triassic of Madagascar, but molecular clock '
                'dating suggests their split from other amphibians may extend further back to the Permian, '
                '265 million years ago. Frogs are widely distributed, ranging from the tropics to subarctic regions',
        'horse': 'The horse (Equus ferus caballus) is a domesticated, odd-toed, hoofed mammal. It belongs to '
                 'the taxonomic family Equidae and is one of two extant subspecies of Equus ferus. The horse has '
                 'evolved over the past 45 to 55 million years from a small multi-toed creature, Eohippus, '
                 'into the large, single-toed animal of today.Horses in the subspecies '
                 'caballus are domesticated, although some domesticated populations live in the wild as feral horses',
        'airplane': "An airplane or aeroplane (informally plane) is a fixed-wing aircraft that is propelled forward "
                    "by thrust from a jet engine, propeller, or rocket engine. Airplanes come in a variety of sizes, "
                    "shapes, and wing configurations. The broad spectrum of uses for airplanes includes recreation, "
                    "transportation of goods and people, military, and research. Worldwide, commercial aviation "
                    "transports more than four billion passengers annually on airliners and transports more than "
                    "200 billion tonne-kilometers of cargo annually, which is less than 1% of the worlds cargo "
                    "movement",
        'ship': "A ship is a large watercraft that travels the world's oceans and other sufficiently deep waterways, "
                "carrying cargo or passengers, or in support of specialized missions, such as defense, research, "
                "and fishing. Ships are generally distinguished from boats, based on size, shape, load capacity, "
                "and purpose. Ships have supported exploration, trade, warfare, migration, colonization, imperialism, "
                "and science. After the 15th century, new crops that had come from and to the Americas via the "
                "European seafarers significantly contributed to world population growth. Ship transport is "
                "responsible for the largest portion of world commerce",
        'truck': "A truck or lorry is a motor vehicle designed to transport cargo, carry specialized payloads, "
                 "or perform other utilitarian work. Trucks vary greatly in size, power, and configuration, "
                 "but the vast majority feature body-on-frame construction, with a cabin that is independent of the "
                 "payload portion of the vehicle. Smaller varieties may be mechanically similar to some automobiles. "
                 "Commercial trucks can be very large and powerful and may be configured to be mounted with "
                 "specialized equipment, such as in the case of refuse trucks, fire trucks, concrete mixers, "
                 "and suction excavators "
    }

    return info_dict[class_name]


