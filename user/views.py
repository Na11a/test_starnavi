from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import LoginView,LogoutView
from .forms import AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate,login
from django.utils import timezone


class LoginView(LoginView):
    template_name = 'user/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('edit_page')
    def get_success_url(self):
        self.request.user.last_login = timezone.now()
        self.request.user.save()
        return self.success_url
        

class RegisterUserView(CreateView):
    model = User
    template_name = 'user/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('edit_page')
    success_msg = 'Well Done'
    def form_valid(self,form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        aut_user = authenticate(username=username,password=password)
        login(self.request, aut_user)
        return form_valid

class Logout(LogoutView):
    next_page = reverse_lazy('home')