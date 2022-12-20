from django.shortcuts import redirect
from .models import Upvote
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError


@login_required
def create(request):
    new_upvote = Upvote()
    new_upvote.review_id = request.POST.get("review_id")
    new_upvote.user_id = request.user.id
    try:
        new_upvote.save()
    except IntegrityError:
        delete_upvote = Upvote.objects.get(
            review_id=new_upvote.review_id,
            user_id=new_upvote.user_id)
        delete_upvote.delete()
    return redirect('/post/{}'.format(int(request.POST.get("post_id"))))

