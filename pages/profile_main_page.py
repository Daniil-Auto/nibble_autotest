from .base_page import BasePage
from .locators import ProfilMainPageLocators
from selenium.webdriver.common.by import By

class ProfileMainPage(BasePage):
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
