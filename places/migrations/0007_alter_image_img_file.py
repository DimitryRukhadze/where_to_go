# Generated by Django 4.1 on 2022-08-13 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_file',
            field=models.ImageField(upload_to='imgs'),
        ),
    ]
