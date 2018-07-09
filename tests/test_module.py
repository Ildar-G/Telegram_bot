import requests
from telebot import misc
import json


token = misc.token
print(token)

URL = 'https://api.telegram.org/bot' + token + '/'
print(URL)


# https://api.telegram.org/bot570286326:AAHITsvlYKNB0YzFJzDGhzRf4lR_st2wsso/sendMessage?chat_id=592689889&text=RU

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    data = r.json()

    with open('test.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    msg = data['result'][-1]['message']['chat']['id']
    print (msg)


get_updates()