from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth import login


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
    return render(request, 'profile/profile.html')