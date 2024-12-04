import time

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class AddCardWomenPage(BasePage):

    PAGE_URL = Links.ADD_CARD_WOMEN

    BUTTON_SIZE = "xpath", "//div[@option-label='S']"
    BUTTON_COLOR = "xpath", "//div[@option-label='Purple']"
    BUTTON_ADD_CARD = "xpath", "//button[@id='product-addtocart-button']"
    CHECK_OUT = "xpath", "//div[@data-block='minicart']"
    EDIT_CARD = "xpath", "(//div[@class='secondary']/a)[2]"
    QTY_CARD_INT = "xpath", "//span[@class='counter-number']"



    def click_color_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_COLOR)).click()

    def click_size_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SIZE)).click()

    def click_button_add_card(self):

        # qty_card = self.wait.until(EC.visibility_of_element_located(self.QTY_CARD_INT))
        # initial_value = int(qty_card.text)
        #
        # self.wait.until(EC.element_to_be_clickable(self.BUTTON_ADD_CARD)).click()
        #
        # def value_change(driver):
        #     update_element = driver.find_element(self.QTY_CARD_INT)
        #     return int(update_element.text) != initial_value
        #
        # updated_card = self.wait.until(EC.visibility_of_element_located(self.QTY_CARD_INT))
        # update_value = int(updated_card.text)
        # assert initial_value == update_value + 1

        qty_card = self.wait.until(EC.visibility_of_element_located(self.QTY_CARD_INT))
        initial_value = int(qty_card.text)

        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ADD_CARD)).click()

        def value_changed(driver):
            updated_element = driver.find_element(*self.QTY_CARD_INT)
            return int(updated_element.text) != initial_value

        self.wait.until(value_changed)

        updated_card = self.wait.until(EC.visibility_of_element_located(self.QTY_CARD_INT))
        updated_value = int(updated_card.text)

        assert updated_value == initial_value + 1


    def click_check_card(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECK_OUT)).click()

    def click_edit_card(self):
        self.wait.until(EC.element_to_be_clickable(self.EDIT_CARD)).click()
