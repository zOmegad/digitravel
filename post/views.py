from django.shortcuts import render
from django.db.models import Avg
from post.models import Post
from comment.models import Comment
from review.models import Review
from django.core.exceptions import ObjectDoesNotExist
from watson import search as watson
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


def index(request):
    item = Post.objects.all()
    item_paginator = Paginator(item, 10)
    page_num = request.GET.get('page')
    try:
        page_obj = item_paginator.page(page_num)
    except (EmptyPage, PageNotAnInteger):
        page_obj = item_paginator.page(1)
    return render(request, 'post/index.html', {'post': page_obj})

def show(request, post_id):
    item = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    try:
        user_review = Review.objects.get(post_id=post_id, user_id=request.user.id)
        reviews = Review.objects.filter(post_id=post_id) # à changer (ne pas inclure le review du current user)
        return render(request, 'post/show.html', 
            {'post': item, 
            'comments': comments,
            'user_review': user_review,
            'reviews': reviews})
    except ObjectDoesNotExist:
        reviews = Review.objects.filter(post_id=post_id)
        return render(request, 'post/show.html', 
            {'post': item, 
            'comments': comments, 
            'reviews': reviews})

def search(request):
    query = request.GET.get('query')
    page_num = request.GET.get('page')
    print(page_num)
    item = watson.filter(Post, query)
    item_paginator = Paginator(item, 10)
    try:
        page_obj = item_paginator.page(page_num)
    except (EmptyPage, PageNotAnInteger):
        page_obj = item_paginator.page(1)

    return render(request, 'post/index.html', {'post': page_obj, 'query': query})