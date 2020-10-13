import pytest
from .pages.lk_base_page import LkBasePage
from .pages.login_page import LoginPage
from .pages.profile_main_page import ProfileMainPage

link = "https://my.nibble.finance/profile.aspx"
class TestUserShouldBeLogin():
    @pytest.fixture(scope="function",autouse=True)
    # Setup авторизация пользователя
    def setup(self, browser):
        login_link = "https://my.nibble.finance//login.aspx"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        email = "daniil.dusya@yandex.ru"
        password = "954514"
        login_page.awtoriz_first_test_user(email, password)
        login_page.should_be_authorized_user

    def test_header_lk(self,browser):
        page = LoginPage(browser, link)
        page.open()
        page_profil = ProfileMainPage(browser, browser.current_url)