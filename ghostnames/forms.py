from django import forms
from ghostnames.models import Username

class UserNameForm(forms.ModelForm):
    class Meta:
        model = Username
        exclude = ['date',]