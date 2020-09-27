import json,  os
import io, configparser

from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, HermesApp

from jokes import Jokes

app = HermesApp("JokesApp")

def read_configuration_file():
    try:
        cp = configparser.ConfigParser()
        with io.open(os.path.dirname(__file__) + "/config.ini", encoding="utf-8") as f:
            cp.read_file(f)
        return {section: {option_name: option for option_name, option in cp.items(section)}
                for section in cp.sections()}
    except (IOError, configparser.Error):
        return dict()

def read_language_file(language):
    try:
        with open(os.path.dirname(__file__) + '/' + language + ".json", 'r') as myfile:
            messages_json_content = myfile.read()

        return json.loads(messages_json_content)
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


@app.on_intent("Joke")
async def Joke(intent: NluIntent):
    sentence = jokes.tell_joke()
    return end_session('Joke', sentence)


if __name__ == "__main__":
    config = read_configuration_file()
    language = read_language_file(config['setup']['language'])
    jokes = Jokes({"language": language["jokes"]})
    app.run()