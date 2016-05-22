from django import forms
from .models import Question, Keyword


class QuestionForm(forms.ModelForm):
    keywords = forms.MultipleChoiceField(
                       required=False,
                       widget=forms.CheckboxSelectMultiple,
                       choices=[(keyword, keyword.keyword) for keyword in Keyword.objects.all()])

    class Meta:
        model = Question
        fields = ['title', 'text', 'keywords']
