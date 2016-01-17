from django.http import HttpResponse


def list_names(request):
    return HttpResponse('hello')