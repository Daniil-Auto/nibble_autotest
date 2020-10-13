from .pages.base_page import BasePage
import time

link = "https://node3.corp.ru/"

def test_login_page(browser):
    page = BasePage(browser, link)   
    page.open()
    time.sleep(3)