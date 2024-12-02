from django.shortcuts import render, redirect
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request,
                  'blog/post-list.html',
                  ctx)


def post_create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    if title and content:
        Post.objects.create(
            title=title,
            content=content
        )
        return redirect('blog:post_list')
    return render(request, 'blog/post-form.html')
