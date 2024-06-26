import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Configura el driver, Chrome
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()