from pages.base_page import BasePage


class InventoryPage(BasePage):
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    INVENTORY_ITEM = ".inventory_item"

    def add_to_cart(self, product_slug):
        self.page.click(f"[data-test='add-to-cart-{product_slug}']")

    def remove_from_cart(self, product_slug):
        self.page.click(f"[data-test='remove-{product_slug}']")

    def get_cart_count(self):
        badge = self.page.locator(self.CART_BADGE)
        if badge.count() == 0:
            return 0
        return int(badge.inner_text())

    def open_cart(self):
        self.page.click(self.CART_LINK)

    def get_product_price(self, product_name):
        item = self.page.locator(self.INVENTORY_ITEM).filter(has_text=product_name)
        price_text = item.locator(".inventory_item_price").inner_text()
        return float(price_text.replace("$", ""))

    def is_loaded(self):
        return self.page.locator(".inventory_list").is_visible()
