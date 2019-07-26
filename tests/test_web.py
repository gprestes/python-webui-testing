import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
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
