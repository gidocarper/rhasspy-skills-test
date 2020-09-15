import logging
import json, random, os
import io, configparser

from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, HermesApp, TopicData

from radio import Radio


app = HermesApp("RadioApp")

def read_configuration_file():
    try:
        cp = configparser.ConfigParser()
        with io.open(os.getcwd() + "/" + os.path.dirname(__file__) + "/config.ini", encoding="utf-8") as f:
            cp.read_file(f)
        return {section: {option_name: option for option_name, option in cp.items(section)}
                for section in cp.sections()}
    except (IOError, configparser.Error):
        return dict()

def read_language_file(language):
    try:
        messages_json_content = open(os.getcwd() + "/" + os.path.dirname(__file__) + '/' + language + '.json')
        return json.load(messages_json_content)
    except:
        return {}

def get_slot_value_by_slot_name(intent, slot_name, default_value):
    jsonString = (NluIntent.to_json(intent))
    jsonIntent = json.loads(jsonString)
    slots = jsonIntent["slots"]

    for i in range(len(slots)):
        if slots[i]['slotName'] == slot_name:
            return slots[i]['value']['value']
    return default_value


def end_session(intent, sentence):
    print('session: ' + intent + ': ' + sentence)
    return EndSession(sentence)


@app.on_intent("PlayInternetRadio")
async def startListening(intent: NluIntent):
    radio_station = get_slot_value_by_slot_name(intent, 'radio_station', None)
    sentence = radio.play_radio_station(radio_station)
    return end_session('Start Listening to Internet Radio', sentence)

@app.on_intent("Stop")
async def stopListening(intent: NluIntent):
    sentence = radio.stop_radio()
    return end_session('Stop Listening to Internet Radio', sentence)


if __name__ == "__main__":
    config = read_configuration_file()
    language = read_language_file(config['setup']['language'])
    print(language)
    radio = Radio({"config": config, "language": language})
    app.run()