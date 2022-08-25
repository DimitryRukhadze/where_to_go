from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = models.TextField()
    description_long = HTMLField(blank=True)
    longitude = models.DecimalField(max_digits=16, decimal_places=14)
    latitude = models.DecimalField(max_digits=16, decimal_places=14)

    def __str__(self):
        return self.title

class Image(models.Model):
    img_file = models.ImageField(upload_to='imgs')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    queue_position = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ['queue_position']

    def __str__(self):
        return f'{self.place.title}_{self.img_file}'