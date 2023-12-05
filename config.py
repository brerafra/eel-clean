import yaml
import os

SETTING_FILE_NAME = "config.yaml"
CONF_DICT = {}

def load_configuration_from_yaml(__yaml_filepath=SETTING_FILE_NAME):
    #Load configurations from config.yaml file
    global CONF_DICT
    try:
        with open(__yaml_filepath) as conf_file:
            CONF_DICT = yaml.safe_load(conf_file.read())
    except Exception as e:
        raise Exception(f'failed to load{__yaml_filepath} due to: {e}')
    
class Config(object):
    #Configurations 
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    load_configuration_from_yaml(os.path.join(BASE_DIR, SETTING_FILE_NAME))

    VERSION = CONF_DICT['version']
    APP_PORT = CONF_DICT['config']['application']['port']
    DB_HOST = CONF_DICT['config']['production']['database_connection_options']['host']
    DB_PORT = CONF_DICT['config']['production']['database_connection_options']['port']
    DB_USER = CONF_DICT['config']['production']['database_connection_options']['user']
    DB_PASS = CONF_DICT['config']['production']['database_connection_options']['pass']
    DB_NAME = CONF_DICT['config']['production']['database_connection_options']['name']
    DB_TIMEOUT = CONF_DICT['config']['production']['database_connection_options']['connect_timeout']