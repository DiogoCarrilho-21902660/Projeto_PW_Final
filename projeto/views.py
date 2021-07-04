from django.shortcuts import render
from .helper import return_graph

from .models import *  # importing all models
from .forms import *  # importing all forms


# Create your views here.
def about_page_view(request):
    return render(request, 'projeto/about.html')


def index_page_view(request):
    return render(request, 'projeto/index.html')


def ourOpinion_page_view(request):
    return render(request, 'projeto/ourOpinion.html')


def multimediaF_page_view(request):
    return render(request, 'projeto/multimediaF.html')


def multimediaV_page_view(request):
    return render(request, 'projeto/multimediaV.html')


def quizz_page_view(request):
    obj = Quiz.objects.all()
    score = 0
    if request.method == 'POST':
        formContact = ContactForm(request.POST)
        formComment = CommentForm(request.POST, request.FILES)
        formSuggestion = SuggestionsForm(request.POST)

        var = request.POST

        for o in obj:
            if o.Answer == var[o.Question]:
                score += 1

        if formComment.is_valid() and formContact.is_valid() and formSuggestion.is_valid():
            user = formContact.save()
            comment = formComment.save(commit=False)
            comment.User = user
            comment.save()
            suggestion = formSuggestion.save(commit=False)
            suggestion.User = user
            suggestion.save()
            Result.objects.create(User=user, Score=score)
    else:
        initial_data = {
            'Primary': "#2c2a2a",
            'Secondary': "#b52121",
            'Text': "#C0C0C0",
        }
        formContact = ContactForm()
        formComment = CommentForm()
        formSuggestion = SuggestionsForm(initial=initial_data)

    if request.method == 'POST':
        context = {
            'formContact': formContact,
            'formComment': formComment,
            'formSuggestion': formSuggestion,
            'obj': obj,
            'graph': return_graph(score, 6 - score)
        }
    else:
        context = {
            'formContact': formContact,
            'formComment': formComment,
            'formSuggestion': formSuggestion,
            'obj': obj,
        }

    return render(request, 'projeto/quizz.html', context)


def tabela_page_view(request):
    return render(request, 'projeto/tabela.html')
