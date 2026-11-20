import re

from playwright.sync_api import Page, expect


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

    def validate_product_title(self, product_name: str = "iPhone 14"):
        expect(
            self.page.get_by_text(product_name, exact=False).first
        ).to_be_visible()

    def validate_cart_button(self):
        add_to_cart = self.page.get_by_role("button", name="Add to cart")

        wishlist = self.page.get_by_text("Wishlist", exact=False)

        assert (add_to_cart.count() > 0 or wishlist.count() > 0), \
            "Neither Add to Cart nor Wishlist was found"

    def add_to_cart(self):
        add_to_cart = self.page.get_by_role(
            "button", name=re.compile(r"add to cart", re.IGNORECASE)
        )

        expect(add_to_cart).to_be_visible()
        add_to_cart.click()