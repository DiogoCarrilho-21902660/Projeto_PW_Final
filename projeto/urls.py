from django.urls import path

from . import views

app_name = 'projeto'

urlpatterns = [
path('', views.index_page_view, name='index'),
path('about/', views.about_page_view, name='about'),
path('ourOpinion/', views.ourOpinion_page_view, name='ourOpinion'),
path('multimediaF/', views.multimediaF_page_view, name='multimediaF'),
path('multimediaV/', views.multimediaV_page_view, name='multimediaV'),
path('quizz/', views.quizz_page_view, name='quizz'),
path('tabela/', views.tabela_page_view, name='tabela'),

]