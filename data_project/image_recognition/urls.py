from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('image_predict', views.image_recognition, name='image')
]