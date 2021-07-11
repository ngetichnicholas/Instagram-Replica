from photos.forms import SearchForm
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Profile
from django.contrib.auth.models import User


# Create your views here.
def index(request):
  search_form = SearchForm()
  current_user = request.user
  profile = Profile.objects.all()
  photos = Image.objects.all().order_by("-posted_at")
  return render(request,'index.html',{'photos':photos,'profile':profile,'form':search_form,'current_user':current_user,})

@login_required(login_url='accounts/login/')
def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')
    else:
        form = PostForm()


    return render(request,'post.html',locals())

def search(request):
  return redirect('home')

def follow(request):
  return redirect('home')

def unfollow(request):
  return redirect('home')

def subscribe(request):
  return redirect('home')

def profile(request):
  return redirect('home')
