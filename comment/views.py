from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from comment.models import Comment

def create(request):
    new_comment = Comment()
    new_comment.body = request.POST.get("comment_body")
    new_comment.user_id = User.objects.get(id=1).id
    new_comment.post_id = int(request.POST.get("post_id"))
    new_comment.save()
    return redirect('/post/1')

def destroy():
    pass
