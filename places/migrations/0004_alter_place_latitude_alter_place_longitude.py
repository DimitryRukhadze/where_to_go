# Generated by Django 4.1 on 2022-08-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_place_latitude_alter_place_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=14, max_digits=16),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=14, max_digits=16),
        ),
    ]
