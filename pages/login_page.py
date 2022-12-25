import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class LoginPage(BasePage):
    WAIT_TIME = 3
    def __init__(self, driver):
        super().__init__(driver)
        self.email_box = (By.CSS_SELECTOR, "[name='email']")
        self.password_box =  (By.CSS_SELECTOR, "[type='password']")
        self.sign_in_btn = (By.CSS_SELECTOR, "[type='submit']")
    def insert_email(self, email):
        self.send_text(self.email_box, email)
    def insert_password(self, user_password):
        self.send_text(self.password_box, user_password)
    def click_submit(self):
        self.click(self.sign_in_btn)

    def perform_login(self, email, user_password):
        self.insert_email(email)
        self.insert_password(user_password)
        self.click_submit()
        time.sleep(self.WAIT_TIME)