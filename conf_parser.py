import yaml
import config

def get_conf():
    with open(config.LANGUAGES_CONF_FILENAME, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
