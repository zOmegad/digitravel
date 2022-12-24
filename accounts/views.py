from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("index") 
    template_name = "registration/signup.html"

    def form_valid(self, form):
            valid = super().form_valid(form)
            login(self.request, self.object)
            return valid

@login_required
def profile(request):
    return render(request, 'profile/profile.html')