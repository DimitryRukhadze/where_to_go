# Generated by Django 4.1 on 2022-08-22 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_alter_image_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='image',
            unique_together=set(),
        ),
    ]
