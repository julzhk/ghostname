from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.cache import cache

from ghostnames.forms import UserNameForm, ChooseGhostNameForm
from ghostnames.models import Username
from ghostnames.models import Ghost

def list_names(request):
    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            newuser = Username.objects.create(
                                    firstname=form.cleaned_data['firstname'],
                                    lastname=form.cleaned_data['lastname']
                                    )
            return HttpResponseRedirect(reverse('choose',
                                                current_app='ghostnames',
                                                args=[newuser.id,]))
    else:
        form = UserNameForm()
    return render(request, 'ghostnames/index.html', {
        'form': form,
        'users':Username.objects.exclude(ghostname='')
    })

def choose_ghost_name(request, uid=None):
    try:
        user = Username.objects.get(id=uid)
    except Username.DoesNotExist:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = ChooseGhostNameForm(request.POST)
        if form.is_valid():
            user.ghostname = form.cleaned_data['ghost_name']
            user.save()
            ghost = Ghost.objects.get(name = form.cleaned_data['ghost_name'])
            ghost.taken = 'taken'
            ghost.save()
            return HttpResponseRedirect(reverse('confirm',
                                                current_app='ghostnames',
                                                args=[user.id,]))

    else:
        form = ChooseGhostNameForm()
    return render(request, 'ghostnames/choosename.html', {
        'form': form,
        'user':user
    })

def confirm_ghost_name(request, uid=None):
    user = Username.objects.get(id=uid)
    return render(request,
                  'ghostnames/confirmname.html', {
                      'user': user
                  })
