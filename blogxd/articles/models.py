from django.db import models
import random

class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='uploads')
    date = models.DateTimeField(auto_now_add=True)
    identifier = models.CharField(max_length=8, editable=False, default='')
    
    def __str__(self):
        return f'{self.identifier}'


def make_id(model):
        generating = True    
        while generating:
            id = ''
            for i in range(8):
                id += str(random.randint(0, 9))

            sc = model.objects.filter(identifier=id)
            if len(sc) > 0:
                pass
            else:
                generating = False
                return id


Article.identifier = make_id(Article)
