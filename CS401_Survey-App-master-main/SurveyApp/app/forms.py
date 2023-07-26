from django.forms import ModelForm
from django import forms
from .models import Poll, Entity, Rating


class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['option_one', 'option_two', 'option_three', 'option_four', 'option_five']

class CreateEntityForm(ModelForm):
    class Meta:
        model = Entity
        fields = ['question']

class CreateRatingQuestionForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rate_question']

