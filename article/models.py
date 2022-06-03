from email.policy import default
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20 , default='all')
    image = models.ImageField(default = "NoImage")

    def __str__(self):
        return self.title
    