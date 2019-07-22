import numpy as np
import os, requests, time
from xml.etree import ElementTree
import playsound as ps
import settings
import requests as req
import wikipediaapi as wikiapi
import numpy as np
import ResponseGen as RG
from os.path import join

subscription_key = settings.getSetting('speech_key')
access_token = ''
wiki = wikiapi.Wikipedia('en')

def __get_token():
    fetch_token_url = "https://northeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    response = requests.post(fetch_token_url, headers=headers)
    return str(response.text)

def __chooseQuestionWord(pageTitle, keywords):
    sections = [s.title for s in wiki.page(pageTitle).sections]
    return sections[0]
    # if len(sections) == 0:
        #     return keywords[0]
        # elif len(sections) == 1:
            #     return sections[0]
            # else:
                #     return sections[np.random.randint(0,len(sections)-1)]

def GenerateQuestion(pageTitle, keywords):
    #question = 'Could you explain the {0} of {1} to me?'.format(__chooseQuestionWord(pageTitle, keywords), pageTitle)
    pageTitle = list(pageTitle.keys())[0] 
    question = 'Could you explain the ' + __chooseQuestionWord(pageTitle, keywords) + ' of ' + pageTitle + ' to me?'
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
    if response.status_code == 200:
        path = r'' + join(os.getcwd(), 'sample-' + timestr + '.wav')
        with open(path, 'wb') as audio:
            audio.write(response.content)
            ps.playsound(path)
        os.remove(path)
    else:
        print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
        
def GenerateNegativeElaboration():
    elaborate_n = RG.elaborate_format
    
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
    voice.text = elaborate_n
    body = ElementTree.tostring(xml_body)

    response = requests.post(constructed_url, headers=headers, data=body)
    print(response.content)
    if response.status_code == 200:
        path = r'' + join(os.getcwd(), 'sample-' + timestr + '.wav')
        with open(path, 'wb') as audio:
            audio.write(response.content)
            ps.playsound(path)
        os.remove(path)
    else:
        print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")

def GenerateAppraise():
    appraise = RG.appraise_format

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
    voice.text = appraise
    body = ElementTree.tostring(xml_body)

    response = requests.post(constructed_url, headers=headers, data=body)
    print(response.content)
    if response.status_code == 200:
        path = r'' + join(os.getcwd(), 'sample-' + timestr + '.wav')
        with open(path, 'wb') as audio:
            audio.write(response.content)
            ps.playsound(path)
        os.remove(path)
    else:
        print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
