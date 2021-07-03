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
    obj = Quiz.objects.all()  # getting all quiz objects to render on quizz.html
    score = 0  # declaring score variable
    if request.method == 'POST':  # conditional statement to check for POST request from frontend
        formContact = ContactForm(request.POST)  # assigning forms
        formComment = CommentForm(request.POST, request.FILES)
        formSuggestion = SuggestionsForm(request.POST)

        var = request.POST  # assigning POST request to a variable to get answers that user entered

        for o in obj:  # loop to store access all answers entered by user
            if o.Answer == var[o.Question]:  # condition to check if users answers match those in db/
                score += 1  # incrementing score of user

        if formComment.is_valid() and formContact.is_valid() and formSuggestion.is_valid(): # condition to check there are no errors in the values user entered
            user = formContact.save()   # storing Contact object in user because, to assign it to the other 2 models
            comment = formComment.save(commit=False)    # commit=False does not store the object unless .save() method is called
            comment.User = user # since Comment model contains FK to Contact model, assigning value to the User field in Comment model
            comment.save()  # saving the object
            suggestion = formSuggestion.save(commit=False)  # commit=False does not store the object unless .save() method is called
            suggestion.User = user # since suggestion model contains FK to Contact model, assigning value to the User field in Comment model
            suggestion.save()   # saving the object
            Result.objects.create(User=user, Score=score)   # saving result for this quiz
    else:   # this is done when the user has not submitted the form or the quizz.html page is being rendered for first time
        initial_data = {                    # these are the color values you had in the web site suggestions option
            'Primary': "#2c2a2a",
            'Secondary': "#b52121",
            'Text': "#C0C0C0",
        }
        formContact = ContactForm()                             # assigning forms to send to html page
        formComment = CommentForm()
        formSuggestion = SuggestionsForm(initial=initial_data)  # the color values to be rendered first time

    if request.method == 'POST':
        context = {
            'formContact': formContact,
            'formComment': formComment,
            'formSuggestion': formSuggestion,
            'obj': obj,
            'graph': return_graph(score, 6 - score)             # calling plotting function and passing it the number of incorrect and correct anwsers value
        }
    else:
        context = {                                             # since graph is not to be rendered in first load so different context dictionaries
            'formContact': formContact,
            'formComment': formComment,
            'formSuggestion': formSuggestion,
            'obj': obj,
        }

    return render(request, 'projeto/quizz.html', context)


def tabela_page_view(request):
    return render(request, 'projeto/tabela.html')
