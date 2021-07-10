from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Profile(models.Model):
  profile_photo = CloudinaryField('image')
  name = CharField(max_length=30)
  bio = TextField()

  def __str__(self):
    return self.name

class Image(models.Model):
  image = CloudinaryField('image')
  image_name = CharField(max_length=30)
  image_caption = CharField(max_length=144)
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  likes = CharField(max_length=10)
  comments = TextField()
  posted_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.image_name



