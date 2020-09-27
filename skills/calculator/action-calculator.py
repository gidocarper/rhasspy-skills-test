import json, os
import io, configparser

from rhasspyhermes.nlu import NluIntent
from rhasspyhermes_app import EndSession, HermesApp

from calculator import Calculator

app = HermesApp("CalculatorApp")

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



############################################### calculator###############################################

@app.on_intent("CalculatorAddition")
async def CalculatorAddition(intent: NluIntent):
    first_value = get_slot_value_by_slot_name(intent, 'first', None)
    second_value = get_slot_value_by_slot_name(intent, 'second', None)
    if (first_value and second_value):
        sentence = calculator.addition(first_value, second_value)
        return end_session('CalculatorAddition', sentence)


@app.on_intent("CalculatorSubstract")
async def CalculatorSubstract(intent: NluIntent):
    first_value = get_slot_value_by_slot_name(intent, 'first', None)
    second_value = get_slot_value_by_slot_name(intent, 'second', None)
    if (first_value and second_value):
        sentence = calculator.subtraction(first_value, second_value)
        return end_session('CalculatorSubstract', sentence)

@app.on_intent("CalculatorMultiply")
async def CalculatorMultiply(intent: NluIntent):
    first_value = get_slot_value_by_slot_name(intent, 'first', None)
    second_value = get_slot_value_by_slot_name(intent, 'second', None)
    if (first_value and second_value):
        sentence = calculator.multiplication(first_value, second_value)
        return end_session('CalculatorMultiply', sentence)

@app.on_intent("CalculatorDivision")
async def CalculatorDivision(intent: NluIntent):
    first_value = get_slot_value_by_slot_name(intent, 'first', None)
    second_value = get_slot_value_by_slot_name(intent, 'second', None)
    if (first_value and second_value):
        sentence = calculator.division(first_value, second_value)
        return end_session('CalculatorDivision', sentence)


@app.on_intent("CalculatorRoot")
async def CalculatorRoot(intent: NluIntent):
    first_value = get_slot_value_by_slot_name(intent, 'first', None)
    if (first_value):
        sentence = calculator.root(first_value)
        return end_session('CalculatorRoot', sentence)


if __name__ == "__main__":
    config = read_configuration_file()
    language = read_language_file(config['setup']['language'])
    calculator = Calculator({"config": config, "language": language})
    app.run()