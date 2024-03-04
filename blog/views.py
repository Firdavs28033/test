from django.shortcuts import render

from .models import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def detail(request, pk):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'detail.html', context)