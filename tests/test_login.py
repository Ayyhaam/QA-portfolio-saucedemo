import re

import pytest
from playwright.sync_api import expect

from tests.conftest import STANDARD_USER, LOCKED_USER, PASSWORD


@pytest.mark.smoke
def test_tc01_login_with_valid_user(login_page, page):
    login_page.login(STANDARD_USER, PASSWORD)
    expect(page).to_have_url(re.compile("inventory.html"))
    expect(page.locator(".title")).to_have_text("Products")


def test_tc02_login_with_wrong_password(login_page):
    login_page.login(STANDARD_USER, "wrong_password")
    expect(login_page.error).to_contain_text(
        "Username and password do not match any user in this service"
    )


def test_tc03_locked_out_user_cannot_login(login_page):
    login_page.login(LOCKED_USER, PASSWORD)
    expect(login_page.error).to_contain_text("Sorry, this user has been locked out")


def test_tc04_login_with_empty_username(login_page):
    login_page.login("", PASSWORD)
    expect(login_page.error).to_contain_text("Username is required")
