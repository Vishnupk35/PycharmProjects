from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=56)
    content=models.CharField(max_length=56)
    author=models.CharField(max_length=50)
    liked_by=models.CharField(max_length=50)
