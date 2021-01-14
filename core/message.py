import requests
from webhook.models import Interaction
from django.conf import settings


def process(json_telegram):
    try:
        try:
            user_id = json_telegram["message"]["from"]["id"]
            text = json_telegram["message"]["text"].split(" ", 1)
        except KeyError:
            user_id = json_telegram["edited_message"]["from"]["id"]
            text = json_telegram["edited_message"]["text"].split(" ", 1)
        command = text[0]
        parm = text[1] if len(text) > 1 else None
        interaction = Interaction.objects.get(input_value=command, active=True)
        binds = interaction.execute(parm)
        output = interaction.get_output(binds)
        return user_id, output
    except Exception:
        return user_id, "Comando Invalido"


def send(user_id, text):
    url = f"https://api.telegram.org/bot{settings.TOKEN_TELEGRAM}/sendMessage"
    data = {"chat_id": user_id, "text": text, "parse_mode": "markdown"}
    requests.post(url, data=data)
