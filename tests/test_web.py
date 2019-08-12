import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.keys import Keys

import json


@pytest.fixture(scope="session")
def config_browser(config):
    if "browser" not in config:
        raise Exception('The config file does not contain "browser"')
    elif config["browser"] not in ["chrome", "firefox"]:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture(scope="session")
def config_wait_time(config):
    return config["wait_time"] if "wait_time" in config else 10


@pytest.fixture(scope="session")
def config():
    with open("tests/config.json") as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture
def browser(config_browser, config_wait_time):
    if config_browser == "chrome":
        driver = Chrome()
    elif config_browser == "firefox":
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    driver.implicitly_wait(config_wait_time)
    yield driver
    driver.quit()


def test_basic_duckduckgo_search(browser):
    PHRASE = "panda"

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
