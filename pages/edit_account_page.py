from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class EditAccPage(BasePage):

    PAGE_URL = Links.EDIT_ACC

    FIRST_NAME_EDIT = "xpath", "//input[@id='firstname']"
    LAST_NAME_EDIT = "xpath", "//input[@id='lastname']"
    BUTTON_SAVE = "xpath", "//button[@title='Save']"
    CONTACT_INFO_FIELD = "xpath", "//div[@class='box-content']/p"

    # _first_name = None
    # _last_name = None

    def edit_first_name(self, new_first_name):
        self._first_name = new_first_name
        first_name = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_EDIT))
        first_name.clear()
        first_name.send_keys(new_first_name)

    def edit_last_name(self, new_last_name):
        self._last_name = new_last_name
        last_name = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_EDIT))
        last_name.clear()
        last_name.send_keys(new_last_name)

    def click_button_save(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SAVE)).click()

    def assert_edit_full_name(self):
        full_name = self.wait.until(EC.visibility_of_element_located(self.CONTACT_INFO_FIELD))
        full_name_edit = full_name.text
        assert full_name_edit == f"{self._first_name} {self._last_name}"