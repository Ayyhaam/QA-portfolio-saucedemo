import pytest
from playwright.sync_api import expect

BACKPACK = "sauce-labs-backpack"


@pytest.mark.smoke
def test_tc09_complete_purchase(logged_in, checkout):
    logged_in.add_to_cart(BACKPACK)
    logged_in.open_cart()
    checkout.start_checkout()
    checkout.fill_information("Test", "Testsson", "12345")
    checkout.finish()
    expect(checkout.complete_header).to_have_text("Thank you for your order!")


def test_tc10_checkout_without_first_name(logged_in, checkout):
    logged_in.add_to_cart(BACKPACK)
    logged_in.open_cart()
    checkout.start_checkout()
    checkout.fill_information("", "Testsson", "12345")
    expect(checkout.error).to_contain_text("First Name is required")
