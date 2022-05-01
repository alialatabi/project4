import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .forms import PostForm
from .models import *


def index(request):
    user = request.user
    posts = Post.objects.order_by('-time_stamp')
    form = PostForm()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/index.html", context={
        'form': form,
        'posts': posts,
        'user': user,
        'page_obj': page_obj
    })


def post(request):
    form = PostForm(request.POST or None)
    user = request.user
    if request.method == "POST":
        if user.is_authenticated:
            if form.is_valid():
                post_text = form.cleaned_data['New_Post']
                Post.objects.create(user=user, post=post_text)

    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


# @csrf_exempt
# def like(request, p_id):
#     if request.method == "GET":
#         return HttpResponseRedirect(reverse("index"))
#
#     if request.method == "POST":
#         data = json.loads(request.body)
#         post_id = data.get('post')
#         user_id = data.get('user')
#         like_filter = Like.objects.filter(post=post_id, user=user_id)
#         if like_filter is not None:
#             like_filter.delete()
#             print('deleted')
#         else:
#             Like.objects.create(post=post_id, user=user_id)
#             print('added')
#         return HttpResponse(status=204)

@login_required(login_url=login_view)
def profile(request, u_name):
    profile_u = User.objects.get(username=u_name)
    user = request.user
    if request.method == 'POST':
        Follower.objects.create(follower=user, following=profile_u)
    posts = Post.objects.filter(user=profile_u).order_by('-time_stamp')
    followers = Follower.objects.filter(following=profile_u).count()
    followings = Follower.objects.filter(follower=profile_u).count()

    return render(request, "network/profile.html", context={
        'posts': posts,
        'user': user,
        'profile_u': profile_u,
        'followers': followers,
        'followings': followings,
    })


def following(request):
    user = request.user
    followings = Follower.objects.filter(follower=user)
    posts = Post.objects.filter(user=None)
    for follow in followings:
        posts |= Post.objects.filter(user=follow.following)
    posts = posts.order_by('-time_stamp')
    return render(request, "network/following.html", context={
        'posts': posts,
        'user': user,
    })
