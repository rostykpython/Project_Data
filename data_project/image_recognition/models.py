from django.db import models


class FileUploaded(models.Model):
    title = models.CharField(max_length=50)
    emp_image = models.ImageField(upload_to='upload/')

