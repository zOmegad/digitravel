from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from comment.models import Comment

@login_required
def create(request):
    new_comment = Comment()
    new_comment.body = request.POST.get("comment_body")
    new_comment.user_id = User.objects.get(id=1).id
    new_comment.post_id = int(request.POST.get("post_id"))
    new_comment.save()
    return redirect('/post/{}'.format(int(request.POST.get("post_id"))))

@login_required
def destroy():
    pass
