from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.register_page import RegisterPage
import pytest

link = "https://nibble.finance/"        

@pytest.mark.login_guest
class TestLoginFromMainPage():
    #Гость видит ссылку на Авторизацию
    def test_guest_should_see_login_link(self,browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    #Гость может перейти на страницу Логина
    def test_guest_can_go_to_login_page(self,browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
        login_window = browser.window_handles[1]
        browser.switch_to.window(login_window)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

class TestRegisterFromMainPage():
    #Гость видит ссылку на Авторизацию
    def test_guest_should_see_register_link(self,browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_register_link()

    #Гость может перейти на страницу Логина
    def test_guest_can_go_to_register_page(self,browser):
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_register_page()          # выполняем метод страницы - переходим на страницу логина
        login_window = browser.window_handles[1]
        browser.switch_to.window(login_window)
        register_page = RegisterPage(browser, browser.current_url)
        register_page.should_be_register_page()
        
@pytest.mark.language
class TestLanguageChange():
    def test_guest_can_change_languages_ru(self,browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_language_dropdown()
        page.language_switcher_ru()
        page_ru = MainPage(browser, browser.current_url)
        page_ru.should_be_ru()
        page.language_switcher_ru_en()
        page.should_be_en()

    def test_guest_can_change_languages_es(self,browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_language_dropdown()
        page.language_switcher_es()
        page_es = MainPage(browser, browser.current_url)
        page_es.should_be_es()
        page.language_switcher_en()
        page.should_be_en()

    def test_guest_can_change_languages_de(self,browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_language_dropdown()
        page.language_switcher_de()
        page_de = MainPage(browser, browser.current_url)
        page_de.should_be_de()
        page.language_switcher_en()
        page.should_be_en()

    def test_guest_can_change_languages_it(self,browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_language_dropdown()
        page.language_switcher_it()
        page_it = MainPage(browser, browser.current_url)
        page_it.should_be_it()
        page.language_switcher_en()
        page.should_be_en()