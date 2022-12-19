from django.shortcuts import render, redirect
from review.models import Review
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    new_review = Review()
    new_review.body = request.POST.get("review_body")
    new_review.score = request.POST.get("review_score")
    new_review.header = request.POST.get("review_header")
    new_review.user_id = request.user.id
    new_review.post_id = int(request.POST.get("post_id"))
    try:
        new_review.save()
    except IntegrityError:
        print("Review already created..")
    return redirect('/post/{}'.format(int(request.POST.get("post_id"))))

@login_required
def destroy(request):
    pass