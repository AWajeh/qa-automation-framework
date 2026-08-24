import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.test_data import VALID_USER, LOCKED_OUT_USER, INVALID_USER


@pytest.mark.smoke
def test_login_with_valid_credentials(page):
    login_page = LoginPage(page).load()
    login_page.login(VALID_USER["username"], VALID_USER["password"])

    inventory_page = InventoryPage(page)
    assert inventory_page.is_loaded()
    assert "inventory" in page.url


@pytest.mark.smoke
def test_login_with_invalid_password(page):
    login_page = LoginPage(page).load()
    login_page.login(INVALID_USER["username"], INVALID_USER["password"])

    assert login_page.is_error_visible()
    assert "do not match" in login_page.get_error_message()


def test_login_with_locked_out_user(page):
    login_page = LoginPage(page).load()
    login_page.login(LOCKED_OUT_USER["username"], LOCKED_OUT_USER["password"])

    assert login_page.is_error_visible()
    assert "locked out" in login_page.get_error_message().lower()
