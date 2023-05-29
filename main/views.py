from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone

# Create your views here.

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    if request.method == 'GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {
            'post':post, 
            'comments':comments,
            })
    elif request.method == "POST":
        new_comment = Comment()
        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()
        new_comment.save()
        return redirect('main:detail', id)

def mainpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts':posts})

def secondpage(request):
    return render(request, 'main/secondpage.html')

def create(request):
    if request.user.is_authenticated:
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.writer = request.user
        new_post.pub_date = timezone.now()
        new_post.body = request.POST['body']
        new_post.weather = request.POST['weather']
        new_post.video = request.POST['video']
        new_post.image = request.FILES.get('image')

        new_post.save()

        return redirect('main:detail', new_post.id)
    
    else :
        return redirect('accounts:login')

def new(request):
    return render(request, 'main/new.html')

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    if request.user.is_authenticated:
        update_post = Post.objects.get(id=id)
        if request.user == update_post.writer:
            update_post.title = request.POST['title']
            update_post.pub_date = timezone.now()
            update_post.body = request.POST['body']
    
            if 'image' in request.FILES:
                update_post.image = request.FILES['image']
           
            update_post.save()
            return redirect('main:detail', update_post.id)

    return redirect('accounts:login')
    
def delete(request, id):
    if request.user.is_authenticated:
        delete_post = get_object_or_404(Post, id=id, writer=request.user)
        delete_post.delete()
        return redirect('main:mainpage')
    return redirect('accounts:login')

def delete_comment(request, id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=id, writer=request.user)
        post_id = comment.post.id
        comment.delete()
        return redirect('main:detail', id=comment.post.id)
    return redirect('accounts:login')
