import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    wait_time = 5
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    driver.implicitly_wait(wait_time)
    yield driver
    driver.close()