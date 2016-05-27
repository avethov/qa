from django.http import HttpResponse, Http404
from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404
from qa.models import Question


def test(request,
         *args,
         **kwargs):
    return HttpResponse('OK')

def test404(request,
         *args,
         **kwargs):
    raise Http404('404')


@require_GET
def new_questions(request):
    list = Question.objects.new()
    page = request.GET.get('page', 1)

    #if not page:
    #    return HttpResponse('OK')


    questions = Question.objects.pagination(list,
                                            page)


    context = {
        'page': questions,
        'questions': questions.object_list,
    }

    return render(request,
                  'list.html',
                  context
                  )


@require_GET
def popular_questions(request):
    list = Question.objects.popular()
    page = request.GET.get('page',
                           1)

    questions = Question.objects.pagination(list,
                                            page)

    context = {
        'page': questions,
        'questions': questions.object_list,
    }

    return render(request,
                  'list.html',
                  context
                  )


@require_GET
def question_details(request,
                     id):
    question = get_object_or_404(Question,
                                 pk=id)

    context = {
        'question': question,
    }

    return render(request,
                  'detail.html',
                  context,
                  )
