from django.shortcuts import render
from post.models import Post


def index(request):
    item = Post.objects.all()
    return render(request, 'post/index.html', {'post': item})

def show(request, post_id):
    item = Post.objects.get(pk=post_id)
    return render(request, 'post/show.html', {'post': item})