import json, re
from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, ContinueSession

def get_slot_value_by_slot_name(intent, slot_name, default_value):

    messurable_units = [
        'money', 'meters', 'inches', 'minutes', 'hours', 'days', 'seconds', 'pieces', 'degrees', 'meters', 'tempurature'
    ]

    jsonString = (NluIntent.to_json(intent))
    jsonIntent = json.loads(jsonString)
    #print('=============================================================================')
    #print(jsonIntent)
    #print('=============================================================================')
    slots = jsonIntent["slots"]

    slotFound = None

    for i in range(len(slots)):
        if slots[i]['slotName'] == slot_name:
            slotFound = slots[i]['value']['value']
            if slot_name in messurable_units:
                return re.findall("\d+", slotFound)[0]

            #print('================================value=============================================')
            #print(slots[i]['value'])
            #print('=================================value============================================')
            return slotFound

    return default_value


def end_session(intent, sentence):
    print('session: ' + intent + ': ' + sentence)
    return EndSession(sentence)