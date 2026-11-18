import pytest
from playwright.sync_api import Page, expect

def sort_products(page: Page, option: str):
    page.on("dialog", lambda dialog: dialog.accept())
    page.select_option(".product_sort_container", option)

@pytest.mark.xfail(reason="b1: every product image is the same pug")
def test_t4_product_images_are_unique(page: Page, login):
    login("problem_user")
    images = page.locator(".inventory_item img")
    sources = [images.nth(i).get_attribute("src") for i in range(images.count())]
    assert len(set(sources)) == len(sources)

@pytest.mark.xfail(reason="b3: sorting is broken for error_user")
def test_t6_sort_name_z_to_a(page: Page, login):
    login("error_user")
    sort_products(page, "za")
    expect(page.locator(".inventory_item_name").first).to_have_text("Test.allTheThings() T-Shirt (Red)")

@pytest.mark.xfail(reason="b3: sorting is broken for error_user")
def test_t7_sort_price_low_to_high(page: Page, login):
    login("error_user")
    sort_products(page, "lohi")
    expect(page.locator(".inventory_item_price").first).to_have_text("$7.99")

@pytest.mark.xfail(reason="b3: sorting is broken for error_user")
def test_t8_sort_price_high_to_low(page: Page, login):
    login("error_user")
    sort_products(page, "hilo")
    expect(page.locator(".inventory_item_price").first).to_have_text("$49.99")

@pytest.mark.xfail(reason="b6: backpack shows a pug image for visual_user")
def test_t12_backpack_has_correct_image(page: Page, login):
    login("visual_user")
    src = page.locator("img[alt='Sauce Labs Backpack']").get_attribute("src")
    assert "backpack" in src

@pytest.mark.xfail(reason="b7: cart button is misaligned for visual_user")
def test_t13_cart_button_aligned(page: Page, login):
    login("standard_user")
    expected = page.locator("#shopping_cart_container").bounding_box()
    page.context.clear_cookies()
    login("visual_user")
    actual = page.locator("#shopping_cart_container").bounding_box()
    assert abs(actual["x"] - expected["x"]) < 5
    assert abs(actual["y"] - expected["y"]) < 5