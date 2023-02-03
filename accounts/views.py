from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import login
from django.contrib.auth.models import User
from review.models import Review
from comment.models import Comment
from django.contrib import messages


class SignUpView(UserPassesTestMixin, generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("index")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid

    def handle_no_permission(self):
        return redirect(reverse("index"))

    def test_func(self):
        return self.request.user.is_anonymous


@login_required
def profile(request):
    user_reviews = Review.objects.filter(user_id=request.user.id)
    user_comments = Comment.objects.filter(user_id=request.user.id)
    return render(
        request,
        "profile/profile.html",
        {"user_reviews": user_reviews, "user_comments": user_comments},
    )


@login_required
def destroy(request):
    current_user = request.user
    if current_user.check_password(request.POST.get("password")):
        db_user = User.objects.get(id=current_user.id)
        current_user.delete()
        db_user.delete()
        messages.success(request, "All your data are destroyed.")
        return redirect("/")
    else:
        messages.error(request, "Password incorrect.")
        return redirect(reverse("profile"))
