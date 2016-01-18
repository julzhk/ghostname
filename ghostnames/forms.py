from django import forms
from ghostnames.models import Username

class UserNameForm(forms.ModelForm):
    class Meta:
        model = Username
        exclude = ['date',]


class ChooseGhostNameForm(forms.Form):
    ghost_name = forms.CharField(label='Your ghost name', max_length=100)