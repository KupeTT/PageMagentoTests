import pytest

from pages.sign_in_page import SingInPage
from pages.my_acc_page import MyAccPage
from pages.edit_account_page import EditAccPage
from pages.create_acc_page import CreateAccPage
from pages.home_page import HomePage
from pages.add_card_women_purple_s_page import AddCardWomenPage

from config.data import Data

class BaseTest:

    data: Data

    add_card_women_page = AddCardWomenPage
    sing_in_page = SingInPage
    my_acc_page = MyAccPage
    create_acc_page = CreateAccPage
    edit_account_page = EditAccPage
    home_page = HomePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.add_card_women_page = AddCardWomenPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.sing_in_page = SingInPage(driver)
        request.cls.my_acc_page = MyAccPage(driver)
        request.cls.create_acc_page = CreateAccPage(driver)
        request.cls.edit_account_page = EditAccPage(driver)
        request.cls.data = Data

