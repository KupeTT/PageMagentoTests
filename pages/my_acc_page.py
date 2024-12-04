
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from config.links import Links

class MyAccPage(BasePage):

    PAGE_URL = Links.MY_ACC_PAGE

    BUTTON_EDIT = "xpath", "(//a[@class='action edit'])[2]"

    def click_edit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_EDIT)).click()
