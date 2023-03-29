from base.baseclass import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class FirstPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__gos_input_num = '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[1]/input'
        self.__gos_input_reg = '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/div/div[2]/input'
        self.__gos_sign_link = '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/span[3]'
        self.__continue_button = '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/button'
        self.__continue_card = '//*[@id="app"]/div[1]/div/div[2]/div/div[2]/form/div[1]'
        self.__sign_link_card = '//*[@id="app"]/div[1]/div/div[2]/div/div[2]'
        self.__fail_gos_input_num = '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]/div/div'

    def get_gos_input_num(self) -> WebElement:
        return self.is_visible('xpath', self.__gos_input_num, 'Gos number')

    def get_gos_input_reg(self) -> WebElement:
        return self.is_visible('xpath', self.__gos_input_reg, 'Gos region')

    def get_gos_sign_link(self) -> WebElement:
        return self.is_visible('xpath', self.__gos_sign_link, 'Gos link')

    def get_continue_button(self) -> WebElement:
        return self.is_visible('xpath', self.__continue_button, 'Cont button')

    def get_continue_card(self) -> WebElement:
        return self.is_visible('xpath', self.__continue_card, 'Form 2')

    def get_sign_link_card(self) -> WebElement:
        return self.is_visible('xpath', self.__sign_link_card, 'Form 2')

    def get_fail_gos_input_num(self) -> WebElement:
        return self.is_visible('xpath', self.__fail_gos_input_num, 'Fail input number')
