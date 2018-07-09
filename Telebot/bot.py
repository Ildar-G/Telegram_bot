import requests
import misc
import json
import weather_api
from time import sleep
key = misc.telegram_key
URL = 'https://api.telegram.org/bot' + key + '/'

global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    current_update_id = data['result'][-1]['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id = data['result'][-1]['message']['chat']['id']
        msg_text = data['result'][-1]['message']['text']

        last_update_id = data['result'][-1]['update_id']
        msg = {'chat_id': chat_id,
               'msg': msg_text,
               'last_update_id': last_update_id}
        return msg
    else:
        return None


def send_message(chat_id, text='wait a sec'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    data = get_updates()

    with open('updates.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['msg']

    while True:
        answer = get_message()
        if answer != None:
            if answer['msg'] == '/weather':
                print(text)
                for i in weather_api.extract_weather('London'):
                    send_message(chat_id, i)
        else:
            continue
        sleep(1)


if __name__ == '__main__':
    main()
