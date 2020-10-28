from django.shortcuts import render,redirect
from .forms import CustomUserChangeForm
from account.models import Account
from main.models import Blog
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def mypage(request):
    blogs = Blog.objects.filter(reemail=request.user.email)
    return render(request, 'mypage.html', {'blogs': blogs})


def profile_update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save() 
            return redirect('mypage')

    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile_update.html',{'user_change_form':user_change_form} )

def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        
        if password_change_form.is_valid():
            user = password_change_form.save()
            update_session_auth_hash(request, user)
            return redirect('mypage')
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'password.html',{ 'password_change_form': password_change_form} )
