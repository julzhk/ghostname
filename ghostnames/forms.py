from django import forms
from ghostnames.models import Username, Ghost

class UserNameForm(forms.ModelForm):
    class Meta:
        model = Username
        exclude = ['date',]

def available_ghosts(sample=3):
    return Ghost.objects.all()[:sample]

class ChooseGhostNameForm(forms.Form):
    ghost_name = forms.ChoiceField(choices=available_ghosts())