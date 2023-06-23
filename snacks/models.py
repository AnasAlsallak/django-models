from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    desc = models.TextField(default='Too much of a yummy thing is a bad thing')
    image = models.ImageField(upload_to='static/', default='static/default.jpg')


    def __str__(self):
        return self.name
    
class Stock(models.Model):
    name = models.CharField(max_length=64)
    admin= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    desc = models.TextField(default='Too much of a yummy thing is a bad thing')
    image = models.ImageField(upload_to='static/', default='static/default.jpg')
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.admin.is_superuser:
            super().save(*args, **kwargs)
        else:
            raise PermissionError("Only admin users can add Stock instances.")