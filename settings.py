import json

def getSetting(key):
    with open('./config.json', 'r') as conf:
        return json.loads(conf.read())[key]
