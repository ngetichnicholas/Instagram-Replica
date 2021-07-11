from photos.forms import SearchForm,PostForm,ProfileForm
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
def post(request):
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

@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    # profile_details = Profile.objects.get(owner_id=current_user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.owner = current_user
            profile.save()
    else:
        form=ProfileForm()

    return render(request, 'profile/profile.html', locals())


@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    user=User.objects.filter(id=id).first()
    profile = user.profile
    profile_details = Profile.get_by_id(id)
    photos = Image.get_profile_images(id)

    usersss = User.objects.get(id=id)
    people=User.objects.all()
    

    return render(request,'profile/profile.html',locals())

def follow(request):
  return redirect('home')

def unfollow(request):
  return redirect('home')

def subscribe(request):
  return redirect('home')
