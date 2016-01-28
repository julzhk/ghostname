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
        self.fields['nickname'] = forms.ChoiceField(
            choices=tuplify_list(available_ghosts()))
        self.fields['nickname'].label = ''

class ChooseNameFormAPI(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ChooseNameFormAPI, self).__init__(*args, **kwargs)
        self.fields['firstname'] = forms.CharField(min_length=2, max_length=20)
        self.fields['lastname'] = forms.CharField(min_length=2, max_length=20)
        self.fields['nickname'] = forms.ChoiceField(
            choices=tuplify_list(available_ghosts()))
        self.fields['nickname'].label = ''
