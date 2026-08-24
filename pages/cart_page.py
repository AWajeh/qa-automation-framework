from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = ".cart_item"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    CHECKOUT_BUTTON = "#checkout"

    def get_item_names(self):
        return self.page.locator(f"{self.CART_ITEM} {self.ITEM_NAME}").all_inner_texts()

    def get_item_prices(self):
        prices = self.page.locator(f"{self.CART_ITEM} {self.ITEM_PRICE}").all_inner_texts()
        return [float(p.replace("$", "")) for p in prices]

    def checkout(self):
        self.page.click(self.CHECKOUT_BUTTON)
