# Generated by Django 4.1 on 2022-08-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_image_queue_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['queue_position']},
        ),
        migrations.AlterField(
            model_name='image',
            name='queue_position',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
