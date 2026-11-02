from playwright.sync_api import Page


class CheckoutPage:
    """Cart page + the checkout steps (your information, overview, complete)."""

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.complete_header = page.locator(".complete-header")
        self.error = page.locator('[data-test="error"]')

    def start_checkout(self):
        self.checkout_button.click()

    def fill_information(self, first: str, last: str, postal: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_button.click()

    def finish(self):
        self.finish_button.click()
