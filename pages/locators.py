from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".account-login")
    REGISTER_LINK = (By.CSS_SELECTOR, ".navigation__item.account-create")
    LOGO = (By.CSS_SELECTOR, ".site-logo")
    USER_ICON =(By.CSS_SELECTOR, ".account")
    BUTTON_LOGOUT = (By.CSS_SELECTOR, ".SignOut > i")
    
    LANGUAGE_DROPDOWN = (By.CSS_SELECTOR, ".language-dropdown__item.active")
    LANG_RU = (By.CSS_SELECTOR, "ul.language-dropdown > li")
    LANG_EN = (By.CSS_SELECTOR, "ul.language-dropdown > li:nth-child(2)")
    LANG_ES = (By.CSS_SELECTOR, "ul.language-dropdown > li:nth-child(2)")
    LANG_DE = (By.CSS_SELECTOR, "ul.language-dropdown > li:nth-child(3)")
    LANG_IT = (By.CSS_SELECTOR, "ul.language-dropdown > li:nth-child(4)")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".account-login")

class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR,".register-wrapper div.box")
    LOGIN_BUTTON = (By.ID, "loginButton")
    LINK_REGISTER = (By.CSS_SELECTOR, "p > .register-link")
    LINK_FORGOT_PASSWORD = (By.CSS_SELECTOR, "p> .register-link:nth-child(2)")
    EMAIL_FIELD = (By.ID, "loginEmail")
    PASSWORD_FIELD = (By.ID, "loginPassword")

class RegisterPageLocators():
    TAB_FORM = (By.CSS_SELECTOR, ".tabs__wrapper")
    
    TAB_COMPANY = (By.CSS_SELECTOR, ".tabs__wrapper > .tab:nth-child(2)")
    FORM_REGISTER_COMPANY = (By.CSS_SELECTOR, "#legalForm>.box")
    COMPANY_NAME_FIELD = (By.CSS_SELECTOR, "legalCompany")
    NAME_OF_HEAD = (By.ID, "legalHead")
    EMAIL_COMPANY_FIELD = (By.ID, "legalEmail")
    CONTINUE_BUTTON = (By.ID, "legalButton")
    
    TAB_INDIVIDUAL = (By.CSS_SELECTOR, ".tabs__wrapper > .tab")
    FORM_REGISTER = (By.CSS_SELECTOR, "#individualForm>.box")
    DROPDOWN_GENDER =(By.CSS_SELECTOR, ".field.field__select")
    FIRST_NAME_FIELD = (By.ID, "individualName")
    EMAIL_FIELD = (By.ID, "individualEmail")
    PROMOCODE_FILED = (By.ID,"individualPromocode")
    REGISTER_BUTTON = (By.ID, "ContentPlaceHolder1_individualButton")
    
    LINK_LOGIN = (By.CSS_SELECTOR, "p>.register-link")

class LkBasePageLocators():
    MY_INVESTMENTS_LINK = (By.CSS_SELECTOR, ".menu>a")
    BALANCE_LINK = (By.CSS_SELECTOR, ".menu>a:nth-child(2)")
    HELP_LINK = (By.CSS_SELECTOR, ".menu>a:nth-child(3)")
    SETTINGS_LINK = (By.CSS_SELECTOR, ".account-settings")
    LOGOUT_LINK = (By.CSS_SELECTOR, ".SignOut")

class ProfilMainPageLocators():
    FORM_CALCULATOR = (By.CSS_SELECTOR,".calculator")
    INITIAL_AMOUNT_FIELD = (By.CSS_SELECTOR, ".calculator__range > .calculator__range-value")
    MONTHLY_DEPOSIT_FIELD = (By.CSS_SELECTOR, ".calculator__range > .calculator__range-value:nth-child(2)")
    PERIOD_FIELD = (By.CSS_SELECTOR, ".calculator__range > .calculator__range-value:nth-child(3)")
    PERCENT = (By.CSS_SELECTOR, ".products-list__key-value.js-calcPercent")
    PROFIT_IN_CALCULATOR = (By.CSS_SELECTOR, "form >ul >li:nth-child(3) > .stat-value")

class SettingsPageLocators():
    PRESONAL_INFORMATION_TAB = (By.CSS_SELECTOR, ".tabs__wrapper> li")
    NAME_FIELD = (By.CSS_SELECTOR, "#settingsName")
    SURNAME_FIELD = (By.CSS_SELECTOR, "#settingsSurname")
    PHONE_FIELD = (By.CSS_SELECTOR, "#settingsPhone")
    BIRTHDAY_FIELD = (By.CSS_SELECTOR, "#settingsBirthday")
    PASSPORT_FIELD = (By.CSS_SELECTOR, "#settingsPassport")
    CITY_FIELD = (By.CSS_SELECTOR, "#settingsCity")
    ADDRESS_1_FIELD = (By.CSS_SELECTOR, "#settingsAddress_1")
    ZIP_FIELD = (By.CSS_SELECTOR, "#settingsZIP")
    BUTTON_PERSONAL_INFORMATION = (By.CSS_SELECTOR, "#btn_person_save")
    
    CHANGE_PASSWORD_TAB = (By.CSS_SELECTOR, ".tabs__wrapper> li:nth-child(2)")
    PASSWORD_CURRENT_FIELD = (By.CSS_SELECTOR, "#settingsPasswordCurrent")
    NEW_PASSWORD_FIELD = (By.CSS_SELECTOR, "#settingsPassNew")
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "#settingsPassRepeat")
    BUTTON_CHANGE_PASSWORD = (By.CSS_SELECTOR, "#btn_password_save")
    
    DETAILS_TAB = (By.CSS_SELECTOR, ".tabs__wrapper> li:nth-child(3)")
    BANK_FIELD = (By.CSS_SELECTOR, "#settingsBank")
    BANK_NUMBER_FIELD = (By.CSS_SELECTOR, "#settingsBankNumber")
    BUTTON_CHANGE_PASSWORD = (By.CSS_SELECTOR, "#btn_password_save")
    
    SETTINGS_TAB = (By.CSS_SELECTOR, ".tabs__wrapper> li:nth-child(4)")
    BUTTON_SETTINGS = (By.CSS_SELECTOR, "#btn_main_save")