from django.db import models
from tinymce.models import HTMLField
from django.core.validators import MinValueValidator, MaxValueValidator


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)
    longitude = models.DecimalField(
        max_digits=17,
        decimal_places=14,
        validators=[MaxValueValidator(180), MinValueValidator(-180)]
    )
    latitude = models.DecimalField(
        max_digits=17,
        decimal_places=14,
        validators=[MaxValueValidator(90), MinValueValidator(-90)]
    )

    def __str__(self):
        return self.title


class Image(models.Model):
    img_file = models.ImageField(upload_to='imgs')
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images'
    )
    queue_position = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['queue_position']

    def __str__(self):
        return f'{self.place.title}_{self.img_file.name}'
