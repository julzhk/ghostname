from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from ghostnames.forms import UserNameForm, ChooseGhostNameForm, available_ghosts, ChooseNameFormAPI
from ghostnames.models import Username
from ghostnames.models import Ghost

import json

class JsonResponse(HttpResponse):
    """
    An HTTP response class that consumes data to be serialized to JSON.

    :param data: Data to be dumped into json. By default only ``dict`` objects
      are allowed to be passed due to a security flaw before EcmaScript 5. See
      the ``safe`` parameter for more information.
    :param encoder: Should be an json encoder class. Defaults to
      ``django.core.serializers.json.DjangoJSONEncoder``.
    :param safe: Controls if only ``dict`` objects may be serialized. Defaults
      to ``True``.
    """

    def __init__(self, data, encoder=json.JSONEncoder, safe=True, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError('In order to allow non-dict objects to be '
                'serialized set the safe parameter to False')
        kwargs.setdefault('content_type', 'application/json')
        data = json.dumps(data, cls=encoder)
        super(JsonResponse, self).__init__(content=data, **kwargs)


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
    release_current_ghost_name(user)
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

def release_current_ghost_name(user):
    # release current users ghost name
    try:
        thisghost = Ghost.objects.get(name=user.ghostname)
        thisghost.taken = 'available'
        thisghost.save()
        user.ghostname = ''
        user.save()
    except Ghost.DoesNotExist:
        pass


def confirm_ghost_name(request, uid=None):
    user = Username.objects.get(id=uid)
    return render(request,
                  'ghostnames/confirmname.html', {
                      'user': user
                  })

def suggestioned_names_api(request):
    if request.method == 'GET':
        names = [{'label':i.name,
                  'value':i.name } for i in available_ghosts()]
        response = JsonResponse(names, safe=False)
    return response

def names_api(request):
    if request.method == 'GET':
        all = [{'firstname': u.firstname,
                'nickname': u.ghostname,
                'lastname': u.lastname
                } for u in Username.objects.all()]
        response = JsonResponse(all, safe=False)
    return response

def register_nickname(request):
    if request.method == 'POST':
        form = ChooseNameFormAPI(json.loads(request.body))
        if form.is_valid():
            user = Username.objects.create(
                                firstname=form.cleaned_data['firstname'],
                                ghostname = form.cleaned_data['nickname'],
                                lastname=form.cleaned_data['lastname']
                                )
            user.save()
            ghost = Ghost.objects.get(name = form.cleaned_data['nickname'])
            ghost.taken = 'taken'
            ghost.save()
            return HttpResponse('ok')
        return HttpResponse('post err')
    return HttpResponse('err')