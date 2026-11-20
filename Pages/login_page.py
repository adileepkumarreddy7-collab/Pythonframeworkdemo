import re

from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.mobile_number_input = page.locator(
            'input[placeholder*="Mobile" i], '
            'input[placeholder*="Email" i], '
            'input[name*="phone" i], '
            'input[type="tel"]'
        ).last

    def open_login_page(self):
        self.page.goto("https://www.flipkart.com/", wait_until="domcontentloaded")
        self.page.get_by_role("link", name="Login").first.click()

    def enter_mobile_number(self, mobile_number: str):
        expect(self.mobile_number_input).to_be_visible()
        self.mobile_number_input.fill(mobile_number)
        expect(self.mobile_number_input).to_have_value(mobile_number)
        self.page.get_by_role(
            "button", name=re.compile(r"continue", re.IGNORECASE)
        ).click()

    def wait_for_otp_and_verify(self, wait_seconds: int = 10):
        self.page.wait_for_timeout(wait_seconds * 1_000)
        self.page.get_by_role(
            "button", name=re.compile(r"verify", re.IGNORECASE)
        ).click()
        expect(self.page).not_to_have_url(re.compile(r"/login(?:[/?#]|$)", re.IGNORECASE))
