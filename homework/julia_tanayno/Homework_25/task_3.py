from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_check_language(driver):
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    select = driver.find_element(By.ID, "id_choose_language")
    language_to_choose = "Ruby"
    dropdown = Select(select)
    dropdown.select_by_visible_text(language_to_choose)
    driver.find_element(By.ID, "submit-id-submit").click()
    result_language = driver.find_element(By.ID, "result-text").text
    assert result_language == language_to_choose


def test_words_hello_world(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.CSS_SELECTOR, "div[id='start'] button").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )
    words = driver.find_element(By.CSS_SELECTOR, "#finish h4").text
    assert words == "Hello World!"
