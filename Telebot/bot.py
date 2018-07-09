import requests
import misc
import json
import weather_api

token = misc.token
print(token)

URL = 'https://api.telegram.org/bot' + token + '/'
print(URL)


# https://api.telegram.org/bot570286326:AAHITsvlYKNB0YzFJzDGhzRf4lR_st2wsso/sendMessage?chat_id=592689889&text=RU

def get_updates():
    url = URL + 'getupdates'
    print(url)
    r = requests.get(url)
    return r.json()



def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    print((chat_id))

    msg_text = data['result'][-1]['message']['text']
    print((msg_text))

    msg = {'chat_id': chat_id,
           'msg': msg_text}
    return msg


def send_message(chat_id, text='wait a sec'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    # print(url)
    requests.get(url)

def send_pic(chat_id, photo='pic/img.png'):
    url = URL + 'sendPhoto?chat_id={}$photo={}'.format(chat_id, photo)
    print(url)
    requests.get(url)



def main():
    data = get_updates()

    with open('updates.json', 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    # print(get_message())

    answer = get_message()
    chat_id = answer['chat_id']
    text = answer['msg']

    send_message(chat_id, 'привет')

    if 'hi' in text:
        send_message(chat_id, "на")

    if 'погода' or 'Погода' in text:
        send_message(chat_id, weather_api.extract_weather('London'))



if __name__ == '__main__':
    main()
