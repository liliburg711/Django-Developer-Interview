from django.db import models
from datetime import datetime

# Create your models here.
class Sale(models.Model):
    title = models.CharField(max_length=500, db_index=True)
    link = models.URLField(max_length=500)
    image = models.ImageField(upload_to='sale/%Y/%m/%d/', blank=True)
    discount = models.CharField(max_length=500, db_index=True)
    price = models.CharField(max_length=500, db_index=True)
    sale_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering=('title',)
        
    def __str__(self):
        return self.title



