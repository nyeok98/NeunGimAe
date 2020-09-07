from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

from account.models import Account


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "phone","nickname","university","student_number", "photo_profil"]