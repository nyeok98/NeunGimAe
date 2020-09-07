from django.shortcuts import render,redirect
from .forms import CustomUserChangeForm
from account.models import Account
from django.contrib.auth.decorators import login_required
# Create your views here.

def mypage(request):
    return render(request, 'mypage.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()        
            return redirect('mypage')

    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile_update.html',{'user_change_form':user_change_form} )
