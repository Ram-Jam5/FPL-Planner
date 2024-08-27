from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    usable_password = None
    
    class Meta:
        model = get_user_model()
        fields = ["username", "password1", "password2"]