from django.shortcuts import render, Http404, get_object_or_404, HttpResponsePermanentRedirect
from django.http import HttpResponse
from .models import Question, Answer
from forms import AskForm, AnswerForm
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
    form = AnswerForm()
    context = {
        'title': question.title,
        'text': question.text,
        'answers': answers,
        'rating': question.rating,
        'from': form,
        }
    return render(request, 'ask/detail.html', context)


def ask_form(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponsePermanentRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask/ask_add.html', {
        'form': form,
    })


def answer_form(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return HttpResponsePermanentRedirect(url)
    else:
        form = AnswerForm()
    return render(request, 'ask/answer_form.html', {
        'form': form,
    })
