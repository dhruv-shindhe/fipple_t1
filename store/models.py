from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(default='default_product.jpg',upload_to='store_pics')
    affiliate_link = models.URLField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.IntegerField(blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store-home')
