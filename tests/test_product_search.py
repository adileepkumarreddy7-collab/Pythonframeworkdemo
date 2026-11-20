from Pages.home_page import HomePage
from Pages.search_page import SearchPage
from Pages.product_page import ProductPage


def test_product_search(page):

    home = HomePage(page)
    search = SearchPage(page)

    # Step 1: Open Flipkart
    home.open_home_page()

    # Step 2: Search iPhone 14
    home.search_product("iPhone 17")

    # Step 3: Validate search results
    search.validate_search_results()

    # Step 4: Apply customer rating filter
    search.apply_rating_filter()

    # Step 5: Open product in new tab
    new_page = search.open_first_product()

    # Step 6: Validate product title
    product = ProductPage(new_page)
    product.validate_product_title()