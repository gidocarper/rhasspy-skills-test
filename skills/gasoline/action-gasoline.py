import json,  os
import io, configparser

from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, HermesApp

from gasoline import Gasoline

app = HermesApp("GasolineApp")

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
        print(os.path.dirname(__file__) + '/' + language + '.json')
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


@app.on_intent("FullPrices")
async def startListening(intent: NluIntent):
    fullType = get_slot_value_by_slot_name(intent, 'fullType', None)
    city = get_slot_value_by_slot_name(intent, 'city', None)
    sentence = ''
    if fullType == "Benzin":
        gasInformation = gasoline.benzin_price(city)
        sentence = gasInformation["sentence"]

    if fullType == "Diesel":
        gasInformation = gasoline.diesel_price(city)
        sentence = gasInformation["sentence"]
    return end_session('Get Gasoline prices', sentence)


if __name__ == "__main__":
    config = read_configuration_file()
    language = read_language_file(config['setup']['language'])
    gasoline = Gasoline({"config": config['gasoline'], "language": language["Gasoline"]})
    app.run()