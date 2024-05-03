import asyncio
from asgiref.sync import sync_to_async

from django import forms
from .models import Feedback
from django.core.mail import mail_admins
from django.utils.translation import gettext_lazy as _

asend_mail = sync_to_async(mail_admins)


async def send_mail_admin(feedback):
    asyncio.create_task(
        asend_mail(
            subject=f' С вами поделились идеей на тему {feedback.theme}!',
            message=
            f'Отправитель: {feedback.name}\n'
            f'Время отправления: {feedback.time_add}\n'
            f'Сообщение: {feedback.message}\n'
            f'Контакты: {feedback.email}\n'
        )
    )


class FeedbackMultipleChoiceForm(forms.ModelForm):
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
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            loop.run_until_complete(send_mail_admin(feedback))
        finally:
            loop.close()
        return feedback
