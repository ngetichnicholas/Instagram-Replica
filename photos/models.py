from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from cloudinary.models import CloudinaryField
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Profile(models.Model):
  profile_photo = CloudinaryField('image')
  username = models.OneToOneField(User,blank=True, on_delete=models.CASCADE, related_name="profile")
  bio = TextField()

  def profile_save(self):
    self.save()

  def delete_profile(self):
    self.delete()

  @classmethod
  def get_by_id(cls, id):
    profile = Profile.objects.get(username=id)
    return profile

  @classmethod
  def get_profile_by_username(cls, username):
    profiles = cls.objects.filter(username__contains=username)
    return profiles

  def __str__(self):
    return self.username

class Image(models.Model):
  image = CloudinaryField('image')
  image_name = CharField(max_length=30)
  image_caption = CharField(max_length=144)
  profile = models.ForeignKey(User, on_delete=models.CASCADE)
  likes = CharField(max_length=10)
  comments = TextField()
  posted_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.image_name



