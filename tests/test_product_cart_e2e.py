from Pages.home_page import HomePage
from Pages.product_page import ProductPage
from Pages.search_page import SearchPage


def test_product_cart_e2e(page):
    home = HomePage(page)
    home.search_product("Samsung Galaxy S25 FE")

    search = SearchPage(page)
    search.validate_search_results("Samsung Galaxy S25 FE")
    product_page = search.open_first_product()

    product = ProductPage(product_page)
    product.validate_product_title("Samsung Galaxy S25 FE")
    product.add_to_cart()
