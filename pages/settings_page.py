from .base_page import BasePage
from .lk_base_page import LkBasePage
from .locators import SettingsPageLocators
from selenium.webdriver.common.by import By

class SettingsPage(BasePage):
    def should_be_setting_page(self):
        self.should_be_setting_url()
        self.should_be_setting_form()

    def should_be_setting_url(self):
        assert 'settings' in self.browser.current_url, "Cant find word SETTINGS in url"
    
    def should_be_setting_form(self):
        assert self.is_element_present(*SettingsPageLocators.PRESONAL_INFORMATION_TAB), "Login form is not presented"

    def change_password(self):
        tab_change_password = self.browser.find_element(*SettingsPageLocators.CHANGE_PASSWORD_TAB)
        tab_change_password.click()
        field_current_password = self.browser.find_element(*SettingsPageLocators.PASSWORD_CURRENT_FIELD)
        field_current_password.send_keys("954514")
        field_new_password = self.browser.find_element(*SettingsPageLocators.NEW_PASSWORD_FIELD)
        field_new_password.send_keys("QwerQwaz")
        field_confirm_password = self.browser.find_element(*SettingsPageLocators.REPEAT_PASSWORD_FIELD)
        field_confirm_password.send_keys("QwerQwaz")
        button_save_password = self.browser.find_element(*SettingsPageLocators.BUTTON_CHANGE_PASSWORD)
        button_save_password.click()