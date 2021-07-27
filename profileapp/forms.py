from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreateForm(ModelForm):
    model = Profile
    fields = ['image', 'nickname', 'message']
