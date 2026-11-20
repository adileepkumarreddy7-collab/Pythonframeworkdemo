from Pages.product_page import ProductPage
from Pages.search_page import SearchPage


def test_product_page(page):
    search = SearchPage(page)

    page.goto("https://www.flipkart.com/search?q=Samsung s25",wait_until="domcontentloaded")
    search.validate_search_results()

    product = ProductPage(search.open_first_product())
    product.validate_product_title()
    product.validate_cart_button()
