from django import forms
from .models import Feedback
from django.core.mail import mail_admins


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name',
            'email',
            'message',
        ]

    def save(self, commit=True):
        feedback = super().save()

        mail_admins(
            subject=f' С вами поделились идеей!',
            message=
                f'Отправитель: {feedback.name}\n'
                f'Время отправления: {feedback.time_add}\n'
                f'Сообщение: {feedback.message}\n'
                f'Контакты: {feedback.email}\n'
        )

        return feedback