from django import forms
from .models import *

class post_create_form(forms.ModelForm):
    class Meta:
        model = post
        fields = '__all__'