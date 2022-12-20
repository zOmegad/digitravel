from django.shortcuts import render
from django.db.models import Avg
from post.models import Post
from comment.models import Comment
from review.models import Review
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    item = Post.objects.all()
    return render(request, 'post/index.html', {'post': item})

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