from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators

class BasePage():
    #Конструктор - метод. Передаём экземпляр драйвера и url адрес.
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    #Открываем нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    #Переходим на страницу Логина
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_register_page(self):
        link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        link.click()

    #Проверяем что пользователь авторизирован
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"

    #Должна быть ссылка на слогин
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_register_link(self):
        assert self.is_element_present(*BasePageLocators.REGISTER_LINK), "Register link is not presented"

    def should_be_language_dropdown(self):
        assert self.is_element_present(*BasePageLocators.LANGUAGE_DROPDOWN), "Language Dropdown is not presented"
    
    #Элемент отсутсвует
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    
    #Элемент исчезает со страницы
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def language_switcher_ru(self):
        language_dropdown = self.browser.find_element(*BasePageLocators.LANGUAGE_DROPDOWN)
        language_dropdown.click()
        switch_to_ru = self.browser.find_element(*BasePageLocators.LANG_RU).click()

    def language_switcher_ru_en(self):
        language_dropdown = self.browser.find_element(*BasePageLocators.LANGUAGE_DROPDOWN)
        language_dropdown.click()
        switch_to_ru_en = self.browser.find_element(*BasePageLocators.LANG_RU).click()

    def language_switcher_en(self):
        language_dropdown = self.browser.find_element(*BasePageLocators.LANGUAGE_DROPDOWN)
        language_dropdown.click()
        switch_to_en = self.browser.find_element(*BasePageLocators.LANG_EN).click()

    def language_switcher_es(self):
        language_dropdown = self.browser.find_element(*BasePageLocators.LANGUAGE_DROPDOWN)
        language_dropdown.click()
        switch_to_es = self.browser.find_element(*BasePageLocators.LANG_ES).click()

    def language_switcher_de(self):
        language_dropdown = self.browser.find_element(*BasePageLocators.LANGUAGE_DROPDOWN)
        language_dropdown.click()
        switch_to_de = self.browser.find_element(*BasePageLocators.LANG_DE).click()

    def language_switcher_it(self):
        language_dropdown = self.browser.find_element(*BasePageLocators.LANGUAGE_DROPDOWN)
        language_dropdown.click()
        switch_to_it = self.browser.find_element(*BasePageLocators.LANG_IT).click()