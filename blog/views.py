from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Post


# Create your views here.
def index(request):
    return render(request, "blog/index.html", {})


def post(request):
    return render(request, "blog/post.html", {})


def posts(request):
    blog_post = Post.objects.all().order_by("-created_at")[:10]

    return render(request, "blog/posts.html", {"blog_post": blog_post})
