from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$',views.index,name='home'),
  url('^search/', views.search, name='search'),
  url(r'^post/$', views.post, name='post'),
  url(r'^subscribe/', views.subscribe, name='subscribe'),
  url(r'^comment/(\d+)', views.comment, name='comment'),
  url(r'^like/(\d+)', views.like, name='like'),
  url(r'^follow/(\d+)', views.follow, name='follow'),
  url(r'^update-profile/',views.update_profile,name ='update-profile'),
  url(r'^accounts/profile/(\d+)',views.profile,name = 'profile'),

]