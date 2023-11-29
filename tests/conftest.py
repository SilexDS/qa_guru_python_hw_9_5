import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 8.0

    # browser.config.type_by_js = True

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'

    # driver_options.add_argument('--headless=new')

    browser.config.driver_options = driver_options

    yield

    browser.quit()
