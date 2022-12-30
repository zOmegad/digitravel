from django.shortcuts import redirect
from review.models import Review
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    new_review = Review()
    new_review.body = request.POST.get("body")
    new_review.header = request.POST.get("header")
    new_review.internet = int(request.POST.get("internet"))
    new_review.hospitality = int(request.POST.get("hospitality"))
    new_review.fun = int(request.POST.get("fun"))
    new_review.cost = int(request.POST.get("cost"))
    new_review.safety = int(request.POST.get("safety"))
    new_review.life_quality = int(request.POST.get("life_quality"))
    new_review.score = (new_review.internet + new_review.hospitality + new_review.fun + new_review.cost + new_review.cost + new_review.life_quality) / 6
    new_review.user_id = request.user.id
    new_review.post_id = int(request.POST.get("post_id"))
    try:
        new_review.save()
    except IntegrityError as e:
        print(e)
    return redirect('/post/{}'.format(int(request.POST.get("post_id"))))

@login_required
def destroy(request):
    delete_review = Review.objects.get(id=int(request.POST.get("review_id")))
    delete_review.delete()
    return redirect('/post/{}'.format(int(request.POST.get("post_id"))))

@login_required
def edit(request):
    edit_review = Review.objects.get(id=int(request.POST.get("review_id")))
    edit_review.internet = request.POST.get("internet")
    edit_review.hospitality = request.POST.get("hospitality")
    edit_review.cost = request.POST.get("cost")
    edit_review.safety = request.POST.get("safety")
    edit_review.life_quality = request.POST.get("life_quality")
    edit_review.fun = request.POST.get("fun")
    edit_review.header = request.POST.get("header")
    edit_review.body = request.POST.get("body")
    try:
        edit_review.save()
    except KeyError as e:
        print(e)
    return redirect('/post/{}'.format(int(request.POST.get("post_id"))))
