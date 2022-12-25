import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from params.parameters import TestParams
@pytest.fixture(autouse=True)
def init_driver(request):
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=options)
    driver.implicitly_wait(10)
    driver.get(TestParams.BASE_URL)
    login = LoginPage(driver)
    login.perform_login(TestParams.EMAIL, TestParams.PASSWORD)
    request.cls.driver = driver

