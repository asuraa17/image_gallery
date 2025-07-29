from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery-list/%Y/%m/%d', blank=False)

    def __str__(self):
        return self.title
