from django.db import models
from .validators import validate_file_extension  # file extension validator
from phonenumber_field.modelfields import PhoneNumberField
import datetime


# Create your models here.

# Contact Class to store Users Name, SurName, Email. Change verbose_name values if you want to show field names in Portuguese
class Contact(models.Model):
    Name = models.CharField(max_length=128, default='Nome', verbose_name='Nome')     # change verbose name of each field to what you want to be displayed in frontend
    SurName = models.CharField(max_length=128, default='Apelido', verbose_name='Apelido')
    Email = models.EmailField(default='exemplo@exemplo.com')
    Phone = PhoneNumberField(default='+351961234567', verbose_name='Contacto')
    DateOfBirth = models.DateField(default=datetime.date.today, verbose_name='Data de Nascimento')

    # method to show Contact Class object's Name, SurName, Email
    def __str__(self):
        return f'{self.Name}{self.SurName}{self.Email}'

    # class Meta to give Names for this db class in admin panel
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'


# class Quiz Contains Question, Correct Answer,4 Answer Choices,
# Choice to select whether quiz is options based or input based
class Quiz(models.Model):
    ANSWER_CHOICES = (
        ('choice', 'choice'),
        ('input', 'input'),
    )
    Question = models.CharField(max_length=1024, default='Questão', verbose_name='Questão')
    Answer = models.CharField(max_length=1024, default='Resposta', verbose_name='Resposta')
    ChoiceOne = models.CharField(max_length=128, default='1ºEscolha', verbose_name='Escolha')
    ChoiceTwo = models.CharField(max_length=128, default='2ºEscolha', verbose_name='Escolha')
    ChoiceThree = models.CharField(max_length=128, default='3ºEscolha', verbose_name='Escolha')
    ChoiceFour = models.CharField(max_length=128, default='4ºEscolha', verbose_name='Escolha')
    Type = models.CharField(max_length=6, choices=ANSWER_CHOICES, default='Escolha')

    def __str__(self):
        return f'{self.Question}{self.Answer}'

    class Meta:
        verbose_name = 'Quiz Pergunta/Resposta'
        verbose_name_plural = 'Quiz Pergunta/Resposta'


# class Result stores the result of each quiz taken
# along with a Foreign Key to the User's Info wo took it, from the Contact's class
class Result(models.Model):
    User = models.ForeignKey(Contact, on_delete=models.CASCADE)
    Score = models.FloatField()

    def __str__(self):
        return f'{self.User}{self.Score}'

    class Meta:
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'


# class Comment contains commentors info, and all the fields you had specified in the form on quizz.html
# File field has a validators paramerter which i have written in validators/py and imported here
# it restricts the user from uploading from any file other than a .txt.
class Comment(models.Model):
    User = models.ForeignKey(Contact, on_delete=models.CASCADE)
    Likeness = models.CharField(max_length=3, default='100',
                                verbose_name='De 0 a 100, quanto gostou deste jogo?')
    GamePlayComment = models.TextField(max_length=5000, default=' ',
                                       verbose_name='Em termos de jogabilidade o que achou?')
    Opinion = models.TextField(max_length=5000, default=' ', verbose_name='Deixe aqui as suas opiniões.')
    File = models.FileField(upload_to='useruploadedfiles/%Y/%m/%d', validators=[validate_file_extension],
                            verbose_name='Qualquer sugestão mais complexa submeta via ficheiro .txt')
    Recommend = models.BooleanField(default=True, verbose_name='Recomendariam este jogo aos seus amigos?')

    def __str__(self):
        return f'{self.User}'

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'


# class Suggestions contains Users info via Foreign Key to Contact class
# and all the relevant fields that were on the quizz.html page
class Suggestions(models.Model):
    User = models.ForeignKey(Contact, on_delete=models.CASCADE)
    Score = models.CharField(max_length=4, default=100,
                             verbose_name='De 0 a 100, quanto gostaram deste website?')
    Primary = models.CharField(max_length=128, default=' ')
    Secondary = models.CharField(max_length=128, default=' ')
    Text = models.CharField(max_length=128, default=' ')

    def __str__(self):
        return f'{self.User}{self.Score}'

    class Meta:
        verbose_name = 'SugestãoWebsite'
        verbose_name_plural = 'SugestõesWebsite'
