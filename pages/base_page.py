import random
import subprocess
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        text = self.driver.find_element(*locator).text
        return text

    def clear_text(self, locator):
        self.driver.find_element(*locator).clear()

    def send_text(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def replace_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL, text)

    def send_text_and_enter(self, locator, text):
        self.driver.find_element(*locator).send_keys(text + Keys.ENTER)

    def check_exist(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def switch_to_new_windows(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)

    def click_js(self, cssSelector):
        self.driver.execute_script("document.querySelector('" + cssSelector + "').click()")

    def click_element_js(self, element):
        self.driver.execute_script("arguments[0].click()", element)

    def send_text_js(self, cssSelector, text):
        self.driver.execute_script("document.querySelector('" + cssSelector + "').value ='" + text + "'")

    # https://stackoverflow.com/questions/25583641/set-value-of-input-instead-of-sendkeys-selenium-webdriver-nodejs
    def send_text_to_element_js(self, element, text):
        self.driver.execute_script("arguments[0].setAttribute('value', '" + text + "')", element)

    def past_text_from_clipboard(self, text):
        subprocess.run("pbcopy", universal_newlines=True, input=text)
        ActionChains(self.driver).key_down(u'\ue03d').key_down('v').perform()


def convert_list_to_lowercase(items):
    new_list = []
    for item in items:
        new_list.append(item.lower())
    return new_list

def get_random_num(min,max):
    rand_num = random.randint(min, max)
    print(f"rand_num: {rand_num}")
    return rand_num
