# Generated by Django 4.0.2 on 2022-07-03 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_recognition', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fileuploaded',
            old_name='emp_image',
            new_name='image',
        ),
    ]
