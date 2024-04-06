from pprint import pprint

from django import forms
from .models import Feedback, Themes
from django.core.mail import mail_admins
from django.utils.translation import gettext_lazy as _


class FeedbackMultipleChoiceForm(forms.ModelForm):

    # theme = forms.ModelMultipleChoiceField(
    #     queryset=Themes.objects.values_list('pk', flat=True), label='Тема', widget=forms.CheckboxSelectMultiple,
    # )


    class Meta:
        model = Feedback
        fields = [
            'name',
            'email',
            'message',
            'theme',
        ]

        labels = {
            'name': _('Имя'),
            'message': _('Сообщение'),
            'theme': _('Тема'),
        }


    def save(self, commit=True):
        feedback = super().save()
        pprint(feedback)
        mail_admins(
            subject=f' С вами поделились идеей!',
            message=
                f'Отправитель: {feedback.name}\n'
                f'Время отправления: {feedback.time_add}\n'
                f'Сообщение: {feedback.message}\n'
                f'Контакты: {feedback.email}\n'
        )

        return feedback