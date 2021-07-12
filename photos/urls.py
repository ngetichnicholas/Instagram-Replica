from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$',views.index,name='home'),
  url(r'^accounts/profile/',views.profile,name='profile'),
  url(r'^search/', views.search, name='search'),
  url(r'^post/$', views.post, name='post'),
  url(r'^like/(\d+)', views.like, name='like'),
  url(r'^follow/(\d+)', views.follow, name='follow'),
  url(r'^update-profile/',views.update_profile,name ='update_profile'),

]