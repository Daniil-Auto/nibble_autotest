from .base_page import BasePage
from .locators import ProfilMainPageLocators
from .locators import LkBasePageLocators
from selenium.webdriver.common.by import By

class ProfileMainPage(BasePage):
    def logout(self):
        logout_button = self.browser.find_element(*LkBasePageLocators.LOGOUT_LINK)
        logout_button.click()

    def go_to_my_investments_page(self):
        link = self.browser.find_element(*LkBasePageLocators.MY_INVESTMENTS_LINK)
        link.click()

    def should_be_investments_page(self):
        assert 'my_investments' in self.browser.current_url, "Cant find words My Investments in url"

    def go_to_balance_page(self):
        link = self.browser.find_element(*LkBasePageLocators.BALANCE_LINK)
        link.click()

    def should_be_balance_page(self):
        assert 'depositing' in self.browser.current_url, "Cant find words Depositing in url"

    def go_to_help_page(self):
        link = self.browser.find_element(*LkBasePageLocators.HELP_LINK)
        link.click()

    def should_be_help_page(self):
        assert 'support' in self.browser.current_url, "Cant find words Support in url"

    def go_to_settings_page(self):
        link = self.browser.find_element(*LkBasePageLocators.SETTINGS_LINK)
        link.click()

    #Расчёт без реинвестирования
    def profit_without_reinvestment(self,initial_amount,monthly_deposit,period):
        initial_field = self.browser.find_element(*ProfilMainPageLocators.INITIAL_AMOUNT_FIELD)
        initial_field.send_keys(initial_amount)
        monthly_deposit_field = self.browser.find_element(*ProfilMainPageLocators.MONTHLY_DEPOSIT_FIELD)
        monthly_deposit_field.send_keys(monthly_deposit)
        period_field = self.browser.find_element(*ProfilMainPageLocators.PERIOD_FIELD)
        period_field.send_keys(period)
        
        percent = self.browser.find_element(*ProfilMainPageLocators.PERCENT)
        percent = int(percent.text[0:2])
        
        initial_amount=1000
        period=12
        monthly_deposit=1000
        your_profit=0
        indicator=0
        for indicator in range(period-3):
            if indicator<=period:
                your_profit=your_profit+(monthly_deposit*percent/365/100)*30.41
                monthly_deposit=monthly_deposit+initial_amount
                indicator=indicator+1
        for indicator in range(0,3):
            your_profit=your_profit+(monthly_deposit*percent/365/100)*30.41
            indicator=indicator+1
        profit_in_calculator = self.browser.find_element(*ProfilMainPageLocators.PROFIT_IN_CALCULATOR)
