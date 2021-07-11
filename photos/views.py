from photos.forms import SearchForm,PostForm,ProfileForm,CommentForm
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Profile,Comment,Like
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

@login_required
def profile(request):
  current_user = request.user
  images = Image.objects.filter(user_id = current_user.id).all()
  
  return render(request,'profile/profile.html',{"images":images,"current_user":current_user})

@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)
    images = Image.get_profile_images(id)

    usersss = User.objects.get(id=id)
    people=User.objects.all()

def search(request):
  return redirect('home')

@login_required(login_url='/login')
def update_profile(request):
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

def follow(request,user_id):
    users=User.objects.get(id=user_id)

    return redirect('accounts/profile/', locals())


def like(request, image_id):
    current_user = request.user
    photos=Image.objects.get(id=image_id)
    new_like,created= Like.objects.get_or_create(liker=current_user, photos=photos)
    new_like.save()

    return redirect('home')

def comment(request,image_id):
    current_user=request.user
    photo = Image.objects.get(id=image_id)
    profile_username = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.photo = photo
            comment.comment_username = current_user
            comment.save()

        return redirect('home')

    else:
        form = CommentForm()

    return render(request, 'comment.html', locals())

def subscribe(request):
  return redirect('home')
