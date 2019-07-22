#!/usr/bin/env python3

import azure.cognitiveservices.speech as speechsdk
import time
import requests
from pprint import pprint # pprint is pretty print (formats the JSON)
from IPython.display import HTML
import settings
import Question
import getWikiData


### Speech recognition
def StartConversation():
    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    speech_key, service_region = settings.getSetting('speech_key'), "northeurope"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    
    # Creates a recognizer with the given settings
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Say something...")
    
    
    result = speech_recognizer.recognize_once()
    
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
    k_ph = key_phrases["documents"][0]["keyPhrases"]
    
    if len(k_ph) > 0:
        top_keywords = getWikiData.most_freq_keyword(KimText,k_ph)
        top_doc, keywords = getWikiData.getWikiData(top_keywords, k_ph,1)
    
    # Recieve information from Kim
    if top_doc != '':
        Question.GenerateQuestion(top_keywords, top_doc)
    
    # Loop conversation
    def SaySome():
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
    
        return(result)
    
    def AnalyzeSome():
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

        k_ph = key_phrases["documents"][0]["keyPhrases"]
        
        if len(k_ph) > 0:
            top_keywords = getWikiData.most_freq_keyword(KimText,k_ph)
            top_doc, keywords = getWikiData.getWikiData(top_keywords, k_ph,1)
        
    # KimConversation is the stored information from conversations
    txtfile = open(top_doc + ".txt","w+")
    KimConversation = result.text
    KimText = result.text
        
    def StoreSome():
        KimConversation = result.text
        KimText = result.text
        # Turn KimConversation into learned information
        # Create or open txt file with topic name
        
        with open(txtfile) as appendtext:
            appendtext.write(KimConversation)
    
    with open (txtfile, "r") as readtext:
        txtdata=readtext.readlines()    
        
    numWords = len(txtdata.split())
    i = 1
    
    import similaritychecker as SCKR
    
    KimActive = True
    if numWords >= 100:
        if SCKR.precision >= 0.5:
            KimActive == False
        elif i >= 10:
            KimActive == False
        else:
            KimActive == True
                
    while KimActive:
        # talk to Kim
        SaySome()
        # save input
        StoreSome()
        # Analyse input
        AnalyzeSome()
        # get new question
        if top_doc != '':
            Question.GenerateQuestion(top_keywords, top_doc)
            i = 1 + i
            # evaluate perfermance and elaborate if precision is below 10 percent.
            # while i > 1:
                #     if SCKR.precision <= 0.1:
                    #         Question.GenerateNegativeElaboration()
                    #     else:
                        #         Question.GenerateAppraise()
                        #         break
                    
        
    
    # Elaborate, evaluate and start conversation
    
    # Flow in conversation
    
          
    
    
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
    # Create or open txt file with topic name
    txtfile = open(top_doc + ".txt","w+")
    
    with open(txtfile) as appendtext:
        appendtext.write(KimConversation)
