from .pages.settings_page import SettingsPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
from .pages.profile_main_page import ProfileMainPage
import pytest

link = "https://my.nibble.finance/"

class TestUserCanLogin():
    @pytest.fixture(scope="function",autouse=True)
    # Setup авторизация пользователя
    def setup(self, browser):
        login_link = "https://back-preprod.nibble.finance/login.aspx"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        email = "levin_d@joy.money"
        password = "954514"
        login_page.awtoriz_first_test_user(email, password)
        login_page.should_be_authorized_user

    def test_guest_can_change_password(self,browser):
        page = LoginPage(browser, link)
        page.open()
        page_profil = ProfileMainPage(browser, browser.current_url)
        page_profil.go_to_settings_page()
        settings_page = SettingsPage(browser, browser.current_url)
        settings_page.change_password()
    