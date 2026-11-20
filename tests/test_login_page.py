from Pages.login_page import LoginPage


def test_login_page_mobile_number(page):
    login = LoginPage(page)

    login.open_login_page()
    login.enter_mobile_number("8008861475")
    login.wait_for_otp_and_verify()
