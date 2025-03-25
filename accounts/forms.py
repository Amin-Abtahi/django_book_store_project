from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# UserCreationForm for SignUp
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age', )
        fields = ('username','age', 'email', )

# UserChangeForm for Admin
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'age', 'email',)