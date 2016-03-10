from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator




def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def new(request):
    try:
        last_questions = Question.odjects.order_by('-id')
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        paginator = Paginator(last_questions, limit)
        paginator.baseurl = '/?page='
        page = paginator.page(page)
    except:
        raise Http404
    return render(request, 'ask/index.html', {
        last_questions: page.odject_list,
        paginator: paginator,
        page: page,
    })



def popular(request):
    try:
        questions = Question.odjects.order_by('-rating')
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        paginator = Paginator(questions, limit)
        paginator.baseurl = '/?page='
        page = paginator.page(page)
    except:
        raise Http404
    return render(request, 'ask/popular.html', {
        questions: page.odject_list,
        paginator: paginator,
        page: page,
    })


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    try:
        answers = Answer.question_set.all()
    except:
        answers = None

    context = {
        'title': question.title,
        'text': question.text,
        'answers': answers,
        }
    return render(request, 'ask/detail.html', context)


