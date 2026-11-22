from playwright.sync_api import expect


def test_addcart_codegen(page):
    close_button = page.get_by_role("button", name="✕")
    if close_button.is_visible():
        close_button.click()

    mobiles = page.get_by_role("link", name="Mobiles")
    expect(mobiles).to_be_visible()
    mobiles.click()
