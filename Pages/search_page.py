import re

from playwright.sync_api import Page, expect


class SearchPage:

    def __init__(self, page: Page):
        self.page = page

    def validate_search_results(self, product_name: str = "iPhone 14"):
        expect(self.page).to_have_url(re.compile(r"[?&]q=", re.IGNORECASE))
        expect(
            self.page.get_by_text(product_name, exact=False).first
        ).to_be_visible()

    def apply_rating_filter(self):
        self.page.get_by_text("Customer Ratings", exact=True).click()
        rating = self.page.get_by_text("4★ & above", exact=False).first

        expect(rating).to_be_visible()
        rating.click()

    def open_first_product(self):
        product = self.page.locator('a[href*="/p/"]').first
        expect(product).to_be_visible()

        with self.page.context.expect_page() as new_page:
            product.click()

        product_page = new_page.value
        product_page.wait_for_load_state("domcontentloaded")
        return product_page