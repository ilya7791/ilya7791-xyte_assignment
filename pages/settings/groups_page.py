import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage, get_random_num
from params.parameters import TestParams

class GroupsPage(BasePage):
    WAIT_TIME = 3
    def __init__(self, driver):
        super().__init__(driver)
        self.createGroup_btn = (By.CSS_SELECTOR, "div:nth-child(2) > button")
        self.groupName_input = (By.CSS_SELECTOR, "[name='name']")
        self.create_btn = (By.CSS_SELECTOR, "[type='submit']")
        self.groups = (By.CSS_SELECTOR, "[role='rowgroup']>div")
        self.addUsers_btn = (By.CSS_SELECTOR, "button[class^='mantine-Button-outline mantine-Button-root mantine']")
        self.addUsers_input = "[placeholder='Add user from this partner']"
        self.search_btn = (By.CSS_SELECTOR, "[placeholder='Search...']")
        self.save_btn ="button.mantine-gnzaph.mantine-Group-child.float-right.d-flex.align-items-center.btn.btn-primary"
        self.group_link = (By.CSS_SELECTOR, "[role='cell']> div > div > svg")
        self.group_users = (By.CSS_SELECTOR, "div[class^='tbody mantine'] div[class^='trow-wrapper mantine']")


    def create_new_group(self, group_name):
        self.click_createGroup_btn()
        self.set_group_name(group_name)
        self.click_create_btn()
        time.sleep(self.WAIT_TIME)

    def add_new_user_for_group(self, group_name, user_name):
        self.search_group(group_name)
        self.click_group()
        self.click_addUsers_btn()
        self.click_addUsers_input_and_add_new_user(user_name)
        self.click_search_btn()
        self.click_save_btn()
        time.sleep(self.WAIT_TIME)
    def get_group_name(self):
        return f"ilya{get_random_num(1,1000)}"

    def check_user_in_group(self, user):
        users_of_group=self.get_elements(self.group_users)
        for user_in_group in users_of_group:
            if user in user_in_group.text:
                return True
        return False

    def click_group(self):
        self.click(self.group_link)

    def search_group(self, group_name):
        self.send_text(self.search_btn, group_name)

    def click_save_btn(self):
        self.click_js(self.save_btn)

    def click_search_btn(self):
        self.click(self.search_btn)

    def set_user_name(self, user_name):
        self.send_text(self.addUsers_input,user_name)

    def click_addUsers_input_and_add_new_user(self,user_name):
        el=self.driver.find_element(By.CSS_SELECTOR, self.addUsers_input)
        el.click()
        el.send_keys(user_name)

    def click_addUsers_btn(self):
        self.click(self.addUsers_btn)

    def check_if_group_exist(self, group_name):
        self.search_group(group_name)
        groups_items=self.get_elements(self.groups )
        for group in groups_items:
            if group_name in group.text:
                return True
        return False

    def click_createGroup_btn(self):
        self.click(self.createGroup_btn)

    def set_group_name(self, group_name):
        self.send_text(self.groupName_input,group_name)

    def click_create_btn(self):
        self.click(self.create_btn)


