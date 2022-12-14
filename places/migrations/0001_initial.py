# Generated by Django 4.1 on 2022-08-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('description_short', models.TextField(blank=True)),
                ('description_long', models.TextField(blank=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=14, max_digits=16)),
                ('latitude', models.DecimalField(blank=True, decimal_places=14, max_digits=16)),
            ],
        ),
    ]
