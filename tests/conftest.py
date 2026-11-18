import pytest
from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture
def login(page: Page):
    def _login(user: str):
        page.goto(BASE_URL)
        page.fill("#user-name", user)
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
    return _login