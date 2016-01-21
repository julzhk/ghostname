from django import forms
from ghostnames.models import Username, Ghost
from ghostnames.utils import tuplify_list


class UserNameForm(forms.ModelForm):
    class Meta:
        model = Username
        exclude = ['date', 'ghostname']

def available_ghosts(sample=3):
    return Ghost.objects.all()[:sample]

class ChooseGhostNameForm(forms.Form):
    ghost_name = forms.ChoiceField(choices=tuplify_list([g.name for g in available_ghosts()]))