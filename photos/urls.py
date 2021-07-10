from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$',views.index,name='home'),
  url('^search/', views.search, name='search'),
  url(r'^follow/(\d+)', views.follow, name='follow'),
  url(r'^unfolow/(\d+)', views.unfollow, name='unfollow'),
  url(r'^subscribe/', views.subscribe, name='subscribe'),
  url(r'^accounts/profile', views.profile,name='user-profile'),

]