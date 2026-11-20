from Pages.home_page import HomePage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.search_page import SearchPage


def test_product_cart_e2e(page):
    login = LoginPage(page)
    login.open_login_page()
    login.enter_mobile_number("8008861475")
    login.wait_for_otp_and_verify(wait_seconds=15)

    home = HomePage(page)
    home.search_product("Samsung Galaxy S25 FE")

    search = SearchPage(page)
    search.validate_search_results("Samsung Galaxy S25 FE")
    product_page = search.open_first_product()

    product = ProductPage(product_page)
    product.validate_product_title("Samsung Galaxy S25 FE")
    product.add_to_cart()
