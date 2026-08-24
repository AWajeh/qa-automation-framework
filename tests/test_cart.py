import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.test_data import BACKPACK, BIKE_LIGHT


@pytest.mark.smoke
def test_add_single_item_updates_cart_badge(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart(BACKPACK)

    assert inventory_page.get_cart_count() == 1


def test_cart_reflects_correct_items_and_prices(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)

    backpack_price = inventory_page.get_product_price("Sauce Labs Backpack")
    bike_light_price = inventory_page.get_product_price("Sauce Labs Bike Light")

    inventory_page.add_to_cart(BACKPACK)
    inventory_page.add_to_cart(BIKE_LIGHT)
    inventory_page.open_cart()

    cart_page = CartPage(logged_in_page)
    item_names = cart_page.get_item_names()
    item_prices = cart_page.get_item_prices()

    assert "Sauce Labs Backpack" in item_names
    assert "Sauce Labs Bike Light" in item_names
    assert sorted(item_prices) == sorted([backpack_price, bike_light_price])
