# CIFAR 10 Classification with Transfer Learning

This project demonstrates using the Keras API to classify images from the [CIFAR-10](https://www.kaggle.com/c/cifar-10) dataset using transfer learning.

### Method
Models used the classify our images is created from the pretrained image classifiers:
* [VGG16](https://keras.io/api/applications/vgg/#vgg16-function)
* [VGG19](https://www.kaggle.com/c/cifar-10)
* [EfficientnetV2](https://keras.io/api/applications/efficientnet_v2/#efficientnetv2b2-function)
* [Xception](https://keras.io/api/applications/xception/)
* [Resnet50](https://keras.io/api/applications/resnet/#resnet50-function)

These networks were originally trained to classify images from the imagenet dataset. This dataset consists of thousands of images divided into 1000 distinct categories.
The CIFAR-10 dataset only has 10 classes so we only want 10 output probabilities.
We upscale our CIFAR-10 dataset from 32x32x3 -> 224x224x3.

### Install application
Using Docker. Download docker_version.zip and unpack archieve folder. Run by 2 commands:
docker-compose build
and

```
docker-compose run -dp 8000:8000 web
```
Download ZIP. Download apllication zip file from repository, unpack it and copy.

### Install Pipenv
Pipenv is a new popular way of automatically creating a 'virtualenv' for the project. It creates Pipfile and Pipfile.lock.
Install it by using pip:

```
pip install pipenv
```
For the application to work corretly, you need to install the neccessary Python libraries. For the installation of the libraries, use the following command:

```
pipenv sync
```
### Database settings
To set up a database connection, enter the necessary settings for connecting to yor database in settings.py located in the application folder.

### Run the application
If everything has been installed correctly, run the development server.
Use the following command:

```
$ python manage.py runserver
```
Open your favorite browser and check at http://127.0.0.1:8000/. You should see a login page that tells you the installation was successfull.

Great :tada: Now to access  the function of the application you need to go through authorization.
