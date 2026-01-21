import pytest

@pytest.fixture
def setup():
    import time
    from selenium import webdriver
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://admin-demo.nopcommerce.com/login')
    yield driver
    driver.close()
