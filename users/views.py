from django.shortcuts import render, redirect
from django.contrib import auth
from main.models import Post

def mypage(request):
    if request.user.is_authenticated:
        user = request.user
        posts = Post.objects.filter(writer=request.user)
        return render(request, 'users/mypage.html', {'posts': posts})

    else:
        return render(request, 'users/login.html')

def post_detail(request, pk):
    post = get.get_object_or_404(Post, pk=pk)
    return render(request, 'main/detail.html', {'post':post})
