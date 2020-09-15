import json
import io, configparser


def read_configuration_file(config_file_path):
    try:
        cp = configparser.ConfigParser()
        with io.open(config_file_path + "/config.ini", encoding="utf-8") as f:
            cp.read_file(f)
        return {section: {option_name: option for option_name, option in cp.items(section)}
                for section in cp.sections()}
    except (IOError, configparser.Error):
        return dict()

def read_language_file(language, language_file_path):
    try:
        messages_json_content = open(language_file_path+ '/' + language + '.json')
        return json.load(messages_json_content)
    except:
        return {}

