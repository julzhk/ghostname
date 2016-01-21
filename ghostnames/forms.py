from django import forms
from ghostnames.models import Username, Ghost
from ghostnames.utils import tuplify_list


class UserNameForm(forms.ModelForm):
    class Meta:
        model = Username
        exclude = ['date', 'ghostname']

def available_ghosts(sample=3):
    return Ghost.objects.filter(taken='available')[:sample]

class ChooseGhostNameForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ChooseGhostNameForm, self).__init__(*args, **kwargs)
        self.fields['ghost_name'] = forms.ChoiceField(
            choices=tuplify_list(available_ghosts()))
        self.fields['ghost_name'].label = ''
