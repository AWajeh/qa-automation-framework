import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.test_data import BACKPACK, BIKE_LIGHT, CHECKOUT_INFO


@pytest.mark.e2e
def test_full_checkout_flow(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_to_cart(BACKPACK)
    inventory_page.add_to_cart(BIKE_LIGHT)
    inventory_page.open_cart()

    cart_page = CartPage(logged_in_page)
    item_prices = cart_page.get_item_prices()
    expected_subtotal = round(sum(item_prices), 2)
    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_customer_info(
        CHECKOUT_INFO["first_name"],
        CHECKOUT_INFO["last_name"],
        CHECKOUT_INFO["postal_code"],
    )

    subtotal = checkout_page.get_subtotal()
    tax = checkout_page.get_tax()
    total = checkout_page.get_total()

    assert subtotal == expected_subtotal
    assert round(subtotal + tax, 2) == round(total, 2)

    checkout_page.finish()
    assert "Thank you" in checkout_page.get_confirmation_message()
