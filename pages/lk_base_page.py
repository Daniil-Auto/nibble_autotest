from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import LkBasePageLocators

class LkBasePage(BasePage):
    def go_to_my_investments_page(self):
        link = self.browser.find_element(*LkBasePageLocators.MY_INVESTMENTS_LINK)
        link.click()

    def go_to_balance_page(self):
        link = self.browser.find_element(*LkBasePageLocators.BALANCE_LINK)
        link.click()

    def go_to_help_page(self):
        link = self.browser.find_element(*LkBasePageLocators.HELP_LINK)
        link.click()

    def go_to_settings_page(self):
        link = self.browser.find_element(*LkBasePageLocators.SETTINGS_LINK)
        link.click()

    def should_be_ru(self):
        button_login = self.browser.find_element(*BasePageLocators.LOGOUT_LINK).text
        assert button_login == "Выход" , "Language do not RU"

    def should_be_en(self):
        button_login = self.browser.find_element(*BasePageLocators.LOGOUT_LINK).text
        assert button_login == "Logout" , "Language do not EN"

    def should_be_es(self):
        button_login = self.browser.find_element(*BasePageLocators.LOGOUT_LINK).text
        assert button_login == "Fin de Sesión" , "Language do not ES"

    def should_be_de(self):
        button_login = self.browser.find_element(*BasePageLocators.LOGOUT_LINK).text
        assert button_login == "Ausloggen" , "Language do not DE"

    def should_be_it(self):
        button_login = self.browser.find_element(*BasePageLocators.LOGOUT_LINK).text
        assert button_login == "Esci" , "Language do not IT"