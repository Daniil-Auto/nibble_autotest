from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Cant find word LOGIN in url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form is not presented"

    #Авторизация пользователя
    def awtoriz_first_test_user(self, email, password):
        enter_email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        enter_email_field.send_keys(email)
        enter_password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        enter_password_field.send_keys(password)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
    