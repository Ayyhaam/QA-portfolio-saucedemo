from playwright.sync_api import Page


class InventoryPage:
    """The product list page that is shown after login."""

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.prices = page.locator(".inventory_item_price")

    def add_to_cart(self, product_id: str):
        self.page.locator(f'[data-test="add-to-cart-{product_id}"]').click()

    def remove_from_cart(self, product_id: str):
        self.page.locator(f'[data-test="remove-{product_id}"]').click()

    def sort_by(self, option: str):
        # Options: "az", "za", "lohi" (price low to high), "hilo" (price high to low)
        self.sort_dropdown.select_option(option)

    def get_prices(self) -> list[float]:
        return [float(p.replace("$", "")) for p in self.prices.all_inner_texts()]

    def open_cart(self):
        self.cart_link.click()
