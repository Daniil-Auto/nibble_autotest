import pytest
from .pages.base_page import BasePage
from .pages.login_page import LoginPage

link = "https://back-preprod.nibble.finance/login.aspx"

class TestUserAddToBasketFromProductPage():
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

#Гость видит ссылку на Авторизацию
def test_guest_should_see_register_link(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_link()

#Гость может перейти на страницу Логина
def test_guest_can_go_to_register_page(browser):
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_register_page()          # выполняем метод страницы - переходим на страницу логина
    login_page = RegisterPage(browser, browser.current_url)
    login_page.should_be_register_page()