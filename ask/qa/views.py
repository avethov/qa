from django.http import HttpResponse, Http404


def test(request,
         *args,
         **kwargs):
    return HttpResponse('OK')

def test404(request,
         *args,
         **kwargs):
    raise Http404('404')
