import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

# Public demo accounts, shown on the SauceDemo start page.
STANDARD_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def logged_in(login_page, page):
    """Start the test already logged in as standard_user."""
    login_page.login(STANDARD_USER, PASSWORD)
    return InventoryPage(page)


@pytest.fixture
def checkout(page):
    return CheckoutPage(page)


API_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api(playwright):
    """An API client (no browser) that talks to the JSONPlaceholder test API."""
    context = playwright.request.new_context(base_url=API_URL)
    yield context
    context.dispose()
