import json
import pytest

from selenium.webdriver import Chrome, Firefox

CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPORTED_BROWSER = ['chrome', 'firefox']

@pytest.fixture(scope='session')
def config():
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def config_browser(config):
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif 