import time

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(BasePage):

    PAGE_URL = Links.HOME_PAGE

    BUTTON_SIZE_1 = "xpath", "//div[@option-label='S']"
    BUTTON_COLOR_1 = "xpath", "//div[@option-label='Purple']"
    CARD_WOMEN = "xpath", "//div[@class='product-item-info']"
    BUTTON_ADD_CARD = "xpath", "//button[@class='action tocart primary']"

    def pointing_сursor(self):
        card = self.wait.until(EC.visibility_of_element_located(self.CARD_WOMEN))
        actions = ActionChains(self.driver)
        actions.move_to_element(card).perform()

    def click_button_size_1(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SIZE_1)).click()

    def click_button_color_1(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SIZE_1)).click()

    def button_add_card(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ADD_CARD)).click()
