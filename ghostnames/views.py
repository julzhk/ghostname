from django.http import HttpResponse
from django.shortcuts import render

from ghostnames.forms import UserNameForm

def list_names(request):
    if request.method == 'POST':
        form = UserNameForm(request.POST)
        if form.is_valid():
            pass
            # Process the data in form.cleaned_data
    else:
        form = UserNameForm() # An unbound form

    return render(request, 'ghostnames/index.html', {
        'form': form,
        'ghostnames':[1,2,3]
    })