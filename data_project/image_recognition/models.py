from django.db import models


class FileUploaded(models.Model):
    class ModelNN(models.TextChoices):
        VGG16 = "1", "VGG16"
        VGG19 = "2", "VGG19"
        DENSENET = "3", "DENSENET"

    model = models.CharField(
        max_length=2,
        choices=ModelNN.choices,
        default=ModelNN.VGG16
    )
    image = models.FileField(upload_to='upload/')

