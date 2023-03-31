import os
from dotenv import load_dotenv
import requests

load_dotenv('.env')


def send_telegram(serializer):
    token = os.getenv('BOT_TOKEN')
    method = 'sendMessage'
    text = 'Вам пришла заявка\n' \
           f'От кого : {serializer.data["fio"]}\n' \
           f'Телефонный номер: {serializer.data["phone_number"]}\n' \
           f'EMAIL : {serializer.data.get("email", "Нет")}\n' \
           f'ЧТО хочет : {serializer.data["text"]}\n'
    requests.post('https://api.telegram.org/bot{0}/{1}'.format(token, method),
                  data={'chat_id': os.getenv('CHAT_ID'), 'text': text}).json()
