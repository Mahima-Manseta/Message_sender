import requests
import json

def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params={
        "authorization" : 'x8CUs4PluhimwEg3WybdSeT6JOrMR9z1HINatqnA2XK7FoQBG0Q2oU4WbItCiywcEuG9JY6mgdLaDRTP',
        'sender_id' : 'FSTSMS',
        'message' : message,
        'language' : 'english'
        'route' : 'p',
        'numbers' : number

    }
response = requests.get(url,params=params)
dic = response.json()
print(dic)

send_sms("8484994288", "test msg")


