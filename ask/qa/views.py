from django.http import HttpRequest

def test(request,
         *args,
         **kwargs):
    return HttpRequest('OK')
