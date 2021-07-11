from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$',views.index,name='home'),
  url('^search/', views.search, name='search'),
  url(r'^post/$', views.post, name='post'),
  url(r'^subscribe/', views.subscribe, name='subscribe'),
  url(r'^accounts/profile', views.profile,name='user-profile'),
  url(r'^comment/(?P<image_id>\d+)', views.comment, name='comment'),
  url(r'^like/(?P<image_id>\d+)', views.like, name='like'),
  url(r'^follow/(?P<user_id>\d+)', views.follow, name='follow'),
  url(r'^update-profile/',views.update_profile,name ='update-profile'),
  url(r'^profile/(?P<id>\d+)',views.profile,name = 'profile'),

]