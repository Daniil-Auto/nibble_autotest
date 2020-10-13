from .base_page import BasePage
from .locators import RegisterPageLocators
from selenium.webdriver.common.by import By

class RegisterPage(BasePage):
    def should_be_register_page(self):
        self.should_be_register_url()
        self.should_be_register_form()

    def should_be_register_url(self):
        assert 'create_account' in self.browser.current_url, "Cant find word Create_account in url"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.FORM_REGISTER), "Register form is not presented"