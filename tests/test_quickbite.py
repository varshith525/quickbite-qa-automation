import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_food_items_page(driver):
    driver.get("https://quickbite-varshith.netlify.app/fooditems/fooditems")

    time.sleep(3)

    assert "/fooditems/fooditems" in driver.current_url

    body_text = driver.find_element(By.TAG_NAME, "body").text

    assert len(body_text) > 0

    time.sleep(5)