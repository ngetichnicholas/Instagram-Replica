from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect


# Create your views here.
def index(request):
  return render(request,'index.html')

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
