from django.db import models
from datetime import datetime
from sellers.models import Seller

class Listing(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    gate = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title
    
