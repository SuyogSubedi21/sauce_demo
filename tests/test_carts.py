import pytest
from playwright.sync_api import Page, expect

@pytest.mark.smoke
def test_standard_user_can_add_to_cart(page: Page, login):
    login("standard_user")
    page.click("#add-to-cart-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

@pytest.mark.xfail(reason="b4: only 3 of 6 products add to cart for error_user")
def test_t9_all_six_products_add_to_cart(page: Page, login):
    login("error_user")
    buttons = page.locator(".inventory_item button")
    for i in range(buttons.count()):
        buttons.nth(i).click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("6")

@pytest.mark.xfail(reason="b5: Remove does nothing on products page for error_user")
def test_t10_remove_works_on_products_page(page: Page, login):
    login("error_user")
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#remove-sauce-labs-backpack")
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)

def test_t11_remove_works_on_cart_page(page: Page, login):
    login("error_user")
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#remove-sauce-labs-backpack")
    expect(page.locator(".cart_item")).to_have_count(0)