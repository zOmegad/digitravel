from django.shortcuts import render
from post.models import Post


def index(request):
    item = Post.objects.all()
    return render(request, 'post/index.html', {'post': item})
