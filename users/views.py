from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
# from django.contrib.auth.models import  User
from .forms import UserLoginForm, UserRegisterForm, ProfileForm
from .models import User


def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request,f'{username},You are now logged in')

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Home - Authorization',
        'form': form
    }
    return render(request,'users/login.html',context)


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username},You are now registered')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Home - Registration',
        'form': form
    }
    return render(request, 'users/registration.html', context)

# class UserRegister(FormView):
#     template_name = 'users/registration.html'
#     form_class = UserRegisterForm
#     success_url = reverse_lazy('users:login')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - Profile',
        'form': form
    }

    return render(request, 'users/profile.html', context)


def users_cart(request):
    return render(request, 'users/users_cart.html')

@login_required
def logout(request):
   messages.success(request, f'{request.user.username},You are now logged out')
   auth.logout(request)
   return redirect(reverse('main:index'))