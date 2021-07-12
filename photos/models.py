from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from cloudinary.models import CloudinaryField
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Profile(models.Model):
  profile_photo = CloudinaryField('photo')
  username = models.OneToOneField(User,on_delete = models.CASCADE)
  bio = models.TextField()

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
  photo = CloudinaryField('image')
  photo_name = CharField(max_length=30)
  photo_caption = models.TextField()
  posted_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User,on_delete = models.CASCADE)

class Comment(models.Model):
  pass

class Like(models.Model):
  pass

class Follows(models.Model):
  pass


