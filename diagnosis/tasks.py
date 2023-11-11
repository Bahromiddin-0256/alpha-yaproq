import requests
from aiogram.exceptions import TelegramBadRequest
from celery import shared_task
from django.conf import settings

from users.models import User


@shared_task()
def send_message_to_user():
    users = User.objects.filter(telegram_id__isnull=False)
    for user in users:
        print(user)
        try:
            requests.post(
                f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?chat_id={user.telegram_id}&text=Hello"
            )
        except requests.ConnectionError:
            pass
    return True
