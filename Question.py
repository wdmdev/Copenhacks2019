import numpy as np
import os, requests, time
from xml.etree import ElementTree
import playsound as ps
import settings

subscription_key = settings.getSetting('sub_key')
access_token = ''

def __get_token():
    fetch_token_url = "https://northeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    response = requests.post(fetch_token_url, headers=headers)
    return str(response.text)

def __chooseQuestionWord(keywords,document):
    verbs = np.array(['is','describe','are'])

    k_score = np.zeros(len(keywords))

    for i, k in enumerate(keywords):
        for v in verbs:
            k_score[i] += document.count('{0} {1}'.format(k,v))

    return keywords[np.argmax(k_score)]

def GenerateQuestion(keywords, document):
    question = '''I heard something about {0},
    could you maybe explain that to me?
    '''.format(__chooseQuestionWord([k.lower() for  k in keywords], document.lower()))
    access_token = __get_token()
    timestr = time.strftime("%Y%m%d-%H%M")

    base_url = 'https://northeurope.tts.speech.microsoft.com/'
    path = 'cognitiveservices/v1'
    constructed_url = base_url + path
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
        'User-Agent': 'Copenhacks2019'
    }
    xml_body = ElementTree.Element('speak', version='1.0')
    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
    voice = ElementTree.SubElement(xml_body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
    voice.set('name', 'Microsoft Server Speech Text to Speech Voice (en-US, Jessa24kRUS)')
    voice.text = question
    body = ElementTree.tostring(xml_body)

    response = requests.post(constructed_url, headers=headers, data=body)
    print(response.content)
    if response.status_code == 200:
        path = 'sample-' + timestr + '.wav'
        with open(path, 'wb') as audio:
            audio.write(response.content)
            ps.playsound(path)
        os.remove(path)
    else:
        print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")


kw = ['linear regression','korea','Ford']
d = 'I know that Korea is using linear regression to take over Ford'
GenerateQuestion(kw, d)
