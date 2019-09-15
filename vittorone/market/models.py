from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    slug = models.SlugField()
    image = models.ImageField(upload_to='item_images/%Y/%m/%d/', default='default.jpg')
    # add id system later

    def __str__(self):
        return f'{self.name} - {self.price}€'

    def snippet(self):
        if len(self.description) > 50:
            return self.description[:50] + '...'
        else:
            return self.description
