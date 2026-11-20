from playwright.sync_api import Page, expect


class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.search_box = page.locator('input[name="q"]:not([readonly])')

    def open_home_page(self):
        self.page.goto("https://www.flipkart.com/", wait_until="domcontentloaded")

    def search_product(self, product_name):
        expect(self.search_box).to_be_visible()
        self.search_box.fill(product_name)
        self.search_box.press("Enter")
