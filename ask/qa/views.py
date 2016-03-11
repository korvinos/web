from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponse
from .models import Question, Answer
from django.core.paginator import Paginator




def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def new(request):
    last_questions = Question.objects.order_by('id')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(last_questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'ask/index.html', {
        'last_questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })



def popular(request):
    questions = Question.objects.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page')
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'ask/popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = Answer.objects.filter(question=question_id)
    context = {
        'title': question.title,
        'text': question.text,
        'answers': answers,
        'rating': question.rating,
        }
    return render(request, 'ask/detail.html', context)


