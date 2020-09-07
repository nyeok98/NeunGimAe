from django.contrib.auth.forms import UserChangeForm
from account.models import Account

from django.contrib.auth import authenticate

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ["email", "username","phone","nickname","university","student_number", "photo_profil"]