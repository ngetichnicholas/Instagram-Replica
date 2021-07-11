from photos.forms import SearchForm,PostForm,UpdateUser,UpdateProfile,CommentForm
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image, Profile,Comment,Like
from django.contrib.auth.models import User
from django.contrib import messages



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
  photos = Image.objects.all().order_by("-posted_at")
  images = Image.objects.filter(user_id = current_user.id).all()
  
  return render(request,'profile/profile.html',{"images":images,'photos':photos,"current_user":current_user})

def search(request):
  return redirect('home')

@login_required
def update_profile(request):
  if request.method == 'POST':
    u_form = UpdateUser(request.POST,instance=request.user)
    p_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    u_form = UpdateUser(instance=request.user)
    p_form = UpdateProfile(instance=request.user.profile) 
  params = {
    'u_form':u_form,
    'p_form':p_form
  }
  return render(request,'profile/update.html',params)


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
