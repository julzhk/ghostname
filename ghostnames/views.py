from django.http import HttpResponse
from django.shortcuts import render

from ghostnames.forms import UserNameForm
from ghostnames.models import Username

def list_names(request):
    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            Username.objects.create(firstname=form.cleaned_data['firstname'],
                                    lastname=form.cleaned_data['lastname']
                                    )
    else:
        form = UserNameForm()

    return render(request, 'ghostnames/index.html', {
        'form': form,
        'ghostnames':Username.objects.all()
    })