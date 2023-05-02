from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=10, min_length=2, error_messages={
#         'max_length': 'Слишком много символов',
#         'min_length': 'Слишком мало символов',
#         'required': 'Должен быть хотя бы 1 символ'
#     })
#     surname = forms.CharField(label='Фамилия', max_length=15, min_length=2)
#     feedback = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows': 5, 'cols': 20}))
#     rating = forms.IntegerField(label='Рейтинг', min_value=1, max_value=5)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname', 'feedback', 'rating']
        # exclude = ['rating']
        fields = '__all__'
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
            'name': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Должен быть хотя бы 1 символ'
            },
            'surname': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Должен быть хотя бы 1 символ'
            },
        }
