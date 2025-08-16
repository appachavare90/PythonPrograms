import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setUp():
    # driver=webdriver.Chrome(ChromeDriverManager().install())
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver