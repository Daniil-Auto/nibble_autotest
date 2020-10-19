from .base_page import BasePage
from .locators import MainPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By

#Создаём класс наследник. предок указывается в скобках.
class MainPage(BasePage):
    #Заглушка т.к. все методы ушли в BasePage
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def should_be_ru(self):
        assert 'ru' in self.browser.current_url, "Cant find word RU in url"
        button_login = self.browser.find_element(*BasePageLocators.LOGIN_LINK).text
        assert button_login == "Вход" , "Language is not RU"

    def should_be_en(self):
        button_login = self.browser.find_element(*BasePageLocators.LOGIN_LINK).text
        assert button_login == "Log in" , "Language is not EN"

    def should_be_es(self):
        assert 'es' in self.browser.current_url, "Cant find word ES in url"
        button_login = self.browser.find_element(*BasePageLocators.LOGIN_LINK).text
        assert button_login == "Entrar" , "Language is not ES"

    def should_be_de(self):
        assert 'de' in self.browser.current_url, "Cant find word DE in url"
        button_login = self.browser.find_element(*BasePageLocators.LOGIN_LINK).text
        assert button_login == "Einloggen" , "Language is not DE"

    def should_be_it(self):
        assert 'it' in self.browser.current_url, "Cant find word IT in url"
        button_login = self.browser.find_element(*BasePageLocators.LOGIN_LINK).text
        assert button_login == "Accedi" , "Language is not IT"