import azure.cognitiveservices.speech as speechsdk
import time
import requests
from pprint import pprint
# pprint is pretty print (formats the JSON)
from IPython.display import HTML
import settings


### Speech recognition

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = settings.getSetting('speech_key'), "northeurope"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")


result = speech_recognizer.recognize_once()
# time.sleep(5)
# speech_recognizer.stop_continuous_recognition()

# Checks result.
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
      
KimText = result.text

### Text analytics - Key Phrases
        
subscription_key = settings.getSetting('text_key')
assert subscription_key

text_analytics_base_url = "https://northeurope.api.cognitive.microsoft.com/text/analytics/v2.0/"

key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)

documents = {'documents' : [
  {'id': '1', 'text': KimText},
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

# Send information to Kim




# Recieve information from Kim




# Elaborate, evaluate and start conversation

# Flow in conversation

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")


result = speech_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Recognized: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
      
# KimConversation is the stored information from conversations
KimConversation = result.text
KimText = result.text

text_analytics_base_url = "https://northeurope.api.cognitive.microsoft.com/text/analytics/v2.0/"

key_phrase_api_url = text_analytics_base_url + "keyPhrases"
print(key_phrase_api_url)

documents = {'documents' : [
  {'id': '1', 'text': KimText},
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

# Turn KimConversation into learned information
