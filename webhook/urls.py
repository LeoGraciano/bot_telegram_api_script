from django.urls import path
from . import views

app_name = 'webhook'

urlpatterns = [
    path('telegram-bot', views.telegram_bot, name='events'),
]
