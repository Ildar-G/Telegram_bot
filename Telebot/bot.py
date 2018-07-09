import requests
import misc
import json

token = misc.token
print(token)

URL = 'https://api.telegram.org/bot' + token + '/'
print(URL)

#https://api.telegram.org/bot570286326:AAHITsvlYKNB0YzFJzDGhzRf4lR_st2wsso/sendMessage?chat_id=592689889&text=RU

def get_updates():
    url = URL + 'getupdates'
    print(url)
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    print((chat_id))

    msg_text =data['result'][-1]['message']['text']
    print((msg_text))

    msg = {'chat_id': chat_id,
           'msg': msg_text}
    return msg

def send_message(chat_id, text = 'wait a sec'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    #print(url)
    requests.get(url)

def main():
  #  d = get_updates()

  #  with open('updates.json', 'w') as file:
  #      json.dump(d, file, ensure_ascii=False, indent=2)

  #print(get_message())

  answer = get_message()
  chat_id = answer['chat_id']
  text = answer['msg']

  send_message(chat_id, 'привет')

  if 'hi' in text:
      send_message(chat_id, "нет")




if __name__ == '__main__':
    main()


