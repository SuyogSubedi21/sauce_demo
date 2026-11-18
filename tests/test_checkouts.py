import pytest
from playwright.sync_api import Page, expect

def checkout(page: Page):
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.fill("#first-name", "Suyog")
    page.fill("#last-name", "Subedi")
    page.fill("#postal-code", "44600")
    page.click("#continue")
    page.click("#finish")

@pytest.mark.smoke
def test_standard_user_can_checkout(page: Page, login):
    login("standard_user")
    checkout(page)
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

@pytest.mark.xfail(reason="b8: Finish at checkout does nothing for error_user")
def test_t14_error_user_can_finish_checkout(page: Page, login):
    login("error_user")
    checkout(page)
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")