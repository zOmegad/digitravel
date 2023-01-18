from django.shortcuts import redirect
from .models import Upvote
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.contrib import messages

@login_required
def create(request):
    new_upvote = Upvote()
    new_upvote.review_id = request.POST.get("review_id")
    new_upvote.user_id = request.user.id
    try:
        new_upvote.save()
        messages.success(request, 'Review upvoted ')
    except IntegrityError:
        # Already upvoted
        messages.error(request, "Review already upvoted ")
        pass
    return redirect('/post/{}'.format(int(request.POST.get("post_id"))))

@login_required
def destroy(request):
    upvote_review = int(request.POST.get("review_id"))
    upvote_user_id = request.user.id
    try:
        upvote = Upvote.objects.get(review_id=upvote_review, user_id=upvote_user_id)
        upvote.delete()
        messages.success(request, 'Upvote destroyed ')
    except ObjectDoesNotExist:
        # never upvoted
        messages.error(request, "Review isn't upvoted ")
        pass
    return redirect('/post/{}'.format(int(request.POST.get("post_id"))))
