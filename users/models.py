from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = fields.ImageField(default = 'default.jpg',upload_to = 'profile_pics',dependencies=[FileDependency(processor=ImageProcessor(format='JPEG', scale={'max_width': 300, 'max_height': 300}))])


    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()  # saving image first
    #
    #     img = Image.open(self.image.path) # Open image using self
    #
    #     if img.height > 300 or img.width > 300:
    #         new_img = (300, 300)
    #         img.thumbnail(new_img)
    #         img.save(self.image.path)  # saving image at the same path
