from django import forms
from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'extenal_id',
            'name',
        )
        widgets = {
            'name': forms.TextInput,
        }
