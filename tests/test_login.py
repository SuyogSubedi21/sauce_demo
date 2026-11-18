import time
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.smoke
def test_t1_standard_user_can_login(page: Page, login):
    login("standard_user")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_t2_wrong_password_shows_error(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    expect(page.locator("[data-test='error']")).to_contain_text("do not match")

def test_t3_locked_out_user_sees_error(page: Page, login):
    login("locked_out_user")
    expect(page.locator("[data-test='error']")).to_contain_text("locked out")

@pytest.mark.xfail(reason="b2: login takes over 5 seconds for performance_glitch_user")
def test_t5_login_is_fast(page: Page, login):
    start = time.time()
    login("performance_glitch_user")
    page.wait_for_url("**/inventory.html")
    assert time.time() - start < 5