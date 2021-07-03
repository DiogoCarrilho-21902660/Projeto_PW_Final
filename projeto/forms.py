from django.forms import ModelForm
from django import forms

from .models import Contact, Comment, Suggestions


# creating model forms here instead of manually creating forms in html
class ContactForm(ModelForm):
    class Meta:
        model = Contact  # class Meta defines a form to the model it is to render
        fields = '__all__'  # specifies that all fields of the model are to be rendered
        widgets = {
            'DateOfBirth': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d')
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment  # model to render
        exclude = ('User',)  # define which field(s) no to render
        widgets = {
            # define widgets and attributes for specific fields to render in html, similar to how these are defined in html
            'Likeness': forms.TextInput(attrs={'type': 'range'}),
            'GamePlayComment': forms.Textarea(attrs={'rows': 15, 'cols': 80}),
            'Opinion': forms.Textarea(attrs={'rows': 15, 'cols': 80}),

        }


class SuggestionsForm(ModelForm):
    class Meta:
        model = Suggestions  # model to render
        exclude = ('User',)  # define which field(s) no to render
        widgets = {
            # define widgets and attributes for specific fields to render in html, similar to how these are defined in html
            'Score': forms.TextInput(attrs={'type': 'range'}),
            'Primary': forms.TextInput(attrs={'type': 'color'}),
            'Secondary': forms.TextInput(attrs={'type': 'color'}),
            'Text': forms.TextInput(attrs={'type': 'color'})
        }
