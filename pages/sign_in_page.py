import time

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SingInPage(BasePage):

    PAGE_URL = Links.SIGN_IN_PAGE

    EMAIL_FIELD = "xpath", "//input[@id='email']"
    PASSWORD_FIELD = "xpath", "//input[@id='pass']"
    SIGN_UP_BUTTON = "xpath", "//div[@class='primary']/button"

    def input_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(email)

    def input_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)


    def click_button_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(self.SIGN_UP_BUTTON)).click()
