from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('email','first_name','last_name','mob_number')

class UserProfileChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('email',)