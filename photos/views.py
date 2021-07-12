from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import Registration,UpdateUser,UpdateProfile,CommentsForm,postPhotoForm
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Like,Follows
from django.http import JsonResponse
from django.contrib.auth.models import User
from .email import send_welcome_email



@login_required(login_url='accounts/login/')
def index(request):
  comment_form = CommentsForm()
  post_form = postPhotoForm()
  photos = Image.display_photos()
  users = User.objects.all()
  
  return render (request,'index.html',{"photos":photos,"comment_form":comment_form,"post":post_form,"all":users})

@login_required
def post(request):
  if request.method == 'POST':
    post_form = postPhotoForm(request.POST,request.FILES) 
    if post_form.is_valid():
      the_post = post_form.save(commit = False)
      the_post.user = request.user
      the_post.save()
      return redirect('home')

  else:
    post_form = postPhotoForm()
  return render(request,'post.html',{"post_form":post_form})

def register(request):
  if request.method == 'POST':
    form = Registration(request.POST)
    if form.is_valid():
      form.save()
      email = form.cleaned_data['email']
      username = form.cleaned_data.get('username')

      messages.success(request,f'Account for {username} created,you can now login')
      return redirect('login')
  else:
    form = Registration()
  return render(request,'registration/registration_form.html',{"form":form})

@login_required
def profile(request):
  current_user = request.user
  photos = Image.objects.all()
  user_photos = Image.objects.filter(user_id = current_user.id).all()
  
  return render(request,'profile/profile.html',{"photos":photos,'user_photos':user_photos,"current_user":current_user})

@login_required
def search(request):
  if 'search_user' in request.GET and request.GET["search_user"]:
    search_term = request.GET.get('search_user')
    users = Profile.search_profiles(search_term)
    photos = Image.search_photos(search_term)
    return render(request,'search.html',{"users":users,"photos":photos})
  else:
    return render(request,'search.html')

@login_required
def likes(request,photo_id):
  if request.method == 'GET':
    photo = Image.objects.get(pk = photo_id)
    user = request.user
    check_user = Like.objects.filter(user = user,photo = photo).first()
    if check_user == None:
      photo = Image.objects.get(pk = photo_id)
      like = Like(like = True,photo = photo,user = user)
      like.save()
      return JsonResponse({'success':True,"img":photo_id,"status":True})
    else:
      check_user.delete()
      return JsonResponse({'success':True,"img":photo_id,"status":False})
 


@login_required
def allcomments(request,photo_id):
  photo = Image.objects.filter(pk = photo_id).first()
  return render(request,'comments.html',{"photo":photo})

@login_required
def users_profile(request,pk):
  comment_form = CommentsForm()
  user = User.objects.get(pk = pk)
  photos = Image.objects.filter(user = user)
  c_user = request.user
  
  return render(request,'profile/users_profile.html',{"user":user,'comment_form':comment_form,
"photos":photos,"c_user":c_user})

@login_required
def update_profile(request):
  if request.method == 'POST':
    user_form = UpdateUser(request.POST,instance=request.user)
    profile_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    user_form = UpdateUser(instance=request.user)
    profile_form = UpdateProfile(instance=request.user.profile) 
  params = {
    'user_form':user_form,
    'profile_form':profile_form
  }
  return render(request,'profile/update.html',params)


@login_required
def unfollow(request,user_id):
  followee = request.user
  follower = Follows.objects.get(pk=user_id)
  follow_data = Follows.objects.filter(follower = follower,followee = followee).first()
  follow_data.delete()
  return redirect('users_profile')

@login_required
def delete(request,photo_id):
  photo = Image.objects.get(pk=photo_id)
  if photo:
    photo.delete_post()
  return redirect('profile')


def like(request, photo_id):
    current_user = request.user
    photos=Image.objects.get(id=photo_id)
    new_like,created= Like.objects.get_or_create(liker=current_user, photos=photos)
    new_like.save()

    return redirect('home')

@login_required
def commenting(request,photo_id):
  c_form = CommentsForm()
  photo = Image.objects.filter(pk = photo_id).first()
  if request.method == 'POST':
    c_form = CommentsForm(request.POST)
    if c_form.is_valid():
      comment = c_form.save(commit = False)
      comment.user = request.user
      comment.photo = photo
      comment.save() 
  return redirect('home')

@login_required
def follow(request,user_id):
  followee = request.user
  followed = Follows.objects.get(pk=user_id)
  follow_data = Follows(follower = followee.profile,followee = followed.profile)
  follow_data.save()
  return redirect('users_profile')
