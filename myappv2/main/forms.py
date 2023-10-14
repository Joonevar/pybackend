from django.contrib.auth.forms import UserChangeForm

from main.models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser