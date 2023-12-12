from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import viewsets
from .serializers import PostSerializer

from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "blog/index.html", {'posts': posts})


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    serializer_class = PostSerializer



class IntruderImage(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer