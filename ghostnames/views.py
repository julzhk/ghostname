from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from ghostnames.forms import UserNameForm, ChooseGhostNameForm
from ghostnames.models import Username

def list_names(request):
    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            Username.objects.create(firstname=form.cleaned_data['firstname'],
                                    lastname=form.cleaned_data['lastname']
                                    )
            return HttpResponseRedirect(reverse('choose',current_app='ghostnames'))
    else:
        form = UserNameForm()

    return render(request, 'ghostnames/index.html', {
        'form': form,
        'ghostnames':Username.objects.all()
    })

def choose_ghost_name(request):
    form = ChooseGhostNameForm()
    return render(request, 'ghostnames/index.html', {
        'form': form,
        'ghostnames':Username.objects.all()
    })
