
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from core import message
import json


@csrf_exempt
@csrf_exempt
def telegram_bot(requests):
    json_telegram = json.loads(requests.body)
    user_id, output = message.process(json_telegram)
    if user_id:
        message.send(user_id, output)
    return HttpResponse()
