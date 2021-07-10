from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Profile(models.Model):
  profile_photo = CloudinaryField('image')
  bio = TextField()

class Image(models.Model):
  image = CloudinaryField('image')
  image_name = CharField(max_length=30)
  image_caption = CharField(max_length=144)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  likes = CharField(max_length=10)
  comments = TextField()
  posted_at = models.DateTimeField(auto_now_add=True)



