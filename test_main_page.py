from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    """ Тест: Гость может перейти на страницу логина """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    """ Тест: Гость видит ссылку на страницу авторизации """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
