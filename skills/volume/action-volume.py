"""Example app using topic for receiving raw MQTT messages."""
import logging
import json, os
import io, configparser

from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, HermesApp
from rhasspyhermes_app import HermesApp, TopicData

from volume import Volume

_LOGGER = logging.getLogger("RawTopicApp")

def read_configuration_file():
    try:
        cp = configparser.ConfigParser()
        print(os.getcwd() + "/" + os.path.dirname(__file__) + "/config.ini")
        with io.open(os.getcwd() + "/" + os.path.dirname(__file__) + "/config.ini", encoding="utf-8") as f:
            cp.read_file(f)
        return {section: {option_name: option for option_name, option in cp.items(section)}
                for section in cp.sections()}
    except (IOError, configparser.Error):
        return dict()

def read_language_file(language):
    try:
        print(os.getcwd() + "/" + os.path.dirname(__file__) + '/' + language + '.json')
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


app = HermesApp("RawTopicApp")



@app.on_topic("hermes/asr/startListening")
async def startListening(data: TopicData, payload: bytes):
    #print(' start listeing')
    volumeControle.mute_volume()
    _LOGGER.debug("topic2: %s, payload: %s", data.topic, payload.decode("utf-8"))


@app.on_topic("hermes/asr/stopListening")
async def stopListening(data: TopicData, payload: bytes):
    #print('stop listeing')
    volumeControle.unmute_volume()
    _LOGGER.debug("topic4: %s, site_id: %s", data.topic, data.data.get("site_id"))

@app.on_intent("VolumeControl")
async def get_date(intent: NluIntent):
    increaseVolume = get_slot_value_by_slot_name(intent, 'increaseVolume', None)
    if increaseVolume:
        sentence = volumeControle.increase_volume()

    decreaseVolume = get_slot_value_by_slot_name(intent, 'decreaseVolume', None)
    if decreaseVolume:
        sentence = volumeControle.decrease_volume()

    scream = get_slot_value_by_slot_name(intent, 'scream', None)
    if scream:
        sentence = volumeControle.set_volume(100)

    whisper = get_slot_value_by_slot_name(intent, 'whisper', None)
    if whisper:
        sentence = volumeControle.set_volume(20)

    volume = get_slot_value_by_slot_name(intent, 'volume', None)
    if volume:
        sentence = volumeControle.set_volume(volume)

    return end_session('VolumeControl', sentence)


if __name__ == "__main__":
    config = read_configuration_file()
    print(config)
    language = read_language_file(config['setup']['language'])
    volumeControle = Volume(language)
    app.run()