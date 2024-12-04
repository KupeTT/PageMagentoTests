from config.links import Links
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CreateAccPage(BasePage):

    PAGE_URL = Links.CREATE_ACC_PAGE

    FIRST_NAME_FIELD = "xpath", "//input[@id='firstname']"
    LAST_NAME_FIELD = "xpath", "//input[@id='lastname']"
    EMAIL_FIELD = "xpath", "//input[@id='email_address']"
    PASSWORD_FIELD = "xpath", "//input[@id='password']"
    CONFIRM_PASSWORD_FIELD = "xpath", "//input[@id='password-confirmation']"
    BUTTON_CREATE = "xpath", "//button[@title='Create an Account']"

    def input_crt_first_name(self, first_name):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD)).send_keys(first_name)

    def input_crt_last_name(self, last_name):
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_FIELD)).send_keys(last_name)

    def input_crt_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(email)

    def input_crt_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def input_crt_confirm_password(self, confirm_password):
        self.wait.until(EC.visibility_of_element_located(self.CONFIRM_PASSWORD_FIELD)).send_keys(confirm_password)

    def click_button_crt(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CREATE)).click()