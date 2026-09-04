import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_quickbite_homepage(driver):
    driver.get("https://quickbite-varshith.netlify.app/")

    assert "QuickBite" in driver.title