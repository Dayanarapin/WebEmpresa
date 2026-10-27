from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post


def blog(request):
    posts = Post.objects.all()
    return render(request, 'core/blog.html', {'posts': posts})