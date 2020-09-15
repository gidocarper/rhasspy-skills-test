import logging
import json, random, os
import io, configparser

from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, HermesApp, TopicData

from dateService import DateService


app = HermesApp("DateApp")

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



############################################### Date and Time ###############################################

@app.on_intent("GetDate")
async def get_date(intent: NluIntent):
    sentence = dateService.whatDayIsIt()
    return end_session('GetDate', sentence)


@app.on_intent("GetTime")
async def get_time(intent: NluIntent):
    sentence = dateService.whatIsTheTime()
    return end_session('GetTime', sentence)


@app.on_intent("whenIsChristmas")
async def when_is_christmas(intent: NluIntent):
    sentence = dateService.whenIsChristmas()
    return end_session('whenIsChristmas', sentence)


if __name__ == "__main__":
    config = read_configuration_file()
    language = read_language_file(config['setup']['language'])
    dateService = DateService({"config": config, "language": language})
    app.run()