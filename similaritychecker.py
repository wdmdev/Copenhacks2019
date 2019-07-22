#!/usr/bin/env python3
import speechsdk as ssdk
import getWikiData as gWD
import numpy as np
import random
import wikipedia as wiki
import azure.cognitiveservices.speech as speechsdk
import time
import requests
from pprint import pprint
from IPython.display import HTML
import settings
import Question
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# Get WikiText
CurriculumText = wiki.page(ssdk.top_doc).content

# Compare texts

subscription_key = settings.getSetting('text_key')
assert subscription_key

text_analytics_base_url = "https://northeurope.api.cognitive.microsoft.com/text/analytics/v2.0/"

key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)

documents = {'documents' : [
  {'id': '1', 'text': ssdk.KimText},
  {'id': '2', 'text': CurriculumText}
]}

headers   = {'Ocp-Apim-Subscription-Key': subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
pprint(key_phrases)

table = []
for document in key_phrases["documents"]:
    text    = next(filter(lambda d: d["id"] == document["id"], documents["documents"]))["text"]    
    phrases = ",".join(document["keyPhrases"])
    table.append("<tr><td>{0}</td><td>{1}</td>".format(text, phrases))
HTML("<table><tr><th>Text</th><th>Key phrases</th></tr>{0}</table>".format("\n".join(table)))

precision = similar(ssdk.KimText,CurriculumText)
