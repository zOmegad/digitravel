from django.shortcuts import render
from django.db.models import Avg
from post.models import Post
from comment.models import Comment
from review.models import Review

def index(request):
    item = Post.objects.all()
    return render(request, 'post/index.html', {'post': item})

def show(request, post_id):
    item = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    reviews = Review.objects.filter(post_id=post_id)
    post_score = reviews.aggregate(avg_rating=Avg('score'))
    return render(request, 'post/show.html', 
        {'post': item, 
        'comments': comments, 
        'reviews': reviews, 
        'post_score': post_score})