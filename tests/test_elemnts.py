import time
import pytest
from pom.firstpage import FirstPage


@pytest.mark.usefixtures('setup')
class TestElements:

    def test_valid_input_gos_num(self):
        firstpage = FirstPage(self.driver)
        firstpage.get_gos_input_num().send_keys('А777АА')
        firstpage.get_gos_input_reg().send_keys('777')
        firstpage.get_continue_button().click()
        time.sleep(5)
        assert firstpage.get_continue_card()

    def test_invalid_input_letters_gos_num(self):
        firstpage = FirstPage(self.driver)
        firstpage.get_gos_input_num().send_keys('Ю001ЮА')
        firstpage.get_gos_input_reg().send_keys('777')
        firstpage.get_continue_button().click()
        time.sleep(5)
        assert firstpage.get_fail_gos_input_num()

    def test_invalid_input_numb_gos_num(self):
        firstpage = FirstPage(self.driver)
        firstpage.get_gos_input_num().send_keys('А000АА')
        firstpage.get_gos_input_reg().send_keys('777')
        firstpage.get_continue_button().click()
        time.sleep(5)
        assert firstpage.get_fail_gos_input_num()

    def test_gos_sign_link(self):
        firstpage = FirstPage(self.driver)
        firstpage.get_gos_sign_link().click()
        time.sleep(5)
        assert firstpage.get_sign_link_card()

    def test_press_continue_button_without_input_gos_num(self):
        firstpage = FirstPage(self.driver)
        firstpage.get_continue_button().click()
        assert firstpage.get_fail_gos_input_num()
