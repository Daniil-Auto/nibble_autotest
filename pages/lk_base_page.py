from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import LkBasePageLocators

class LkBasePage(BasePage):
    

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