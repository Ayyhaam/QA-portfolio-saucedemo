import pytest
from playwright.sync_api import expect

BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"


@pytest.mark.smoke
def test_tc05_add_product_to_cart(logged_in):
    logged_in.add_to_cart(BACKPACK)
    expect(logged_in.cart_badge).to_have_text("1")


def test_tc06_add_two_products_to_cart(logged_in):
    logged_in.add_to_cart(BACKPACK)
    logged_in.add_to_cart(BIKE_LIGHT)
    expect(logged_in.cart_badge).to_have_text("2")


def test_tc07_remove_product_from_cart(logged_in):
    logged_in.add_to_cart(BACKPACK)
    logged_in.remove_from_cart(BACKPACK)
    expect(logged_in.cart_badge).to_have_count(0)


def test_tc08_sort_by_price_low_to_high(logged_in):
    logged_in.sort_by("lohi")
    prices = logged_in.get_prices()
    assert prices == sorted(prices), f"Prices are not sorted: {prices}"
