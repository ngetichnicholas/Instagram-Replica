from django.test import TestCase

# Create your tests here.
class TestComments(TestCase):

  def setUp(self):
    self.test_user = User(username = 'Nicholas')
    self.test_user.save()
    self.photo = Image(photo = 'new_photo.png',photo_name = 'software image',photo_caption = 'software engineer',user = self.test_user)
    self.comments = Comment(comment = 'Nice one',photo = self.photo,user = self.test_user)