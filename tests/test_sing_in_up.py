from base.base_test import BaseTest

class TestSing(BaseTest):

    def test_sign_in(self):

        self.sing_in_page.open()
        self.sing_in_page.is_open()
        self.sing_in_page.input_email(self.data.EMAIL)
        self.sing_in_page.input_password(self.data.PASSWORD)
        self.sing_in_page.click_button_sign_in()
        self.home_page.is_open()
        self.home_page.pointing_сursor()
        self.home_page.button_add_card()
        self.add_card_women_page.is_open()
        self.add_card_women_page.click_color_button()
        self.add_card_women_page.click_size_button()
        self.add_card_women_page.click_button_add_card()
        self.add_card_women_page.click_check_card()
        self.add_card_women_page.click_edit_card()



