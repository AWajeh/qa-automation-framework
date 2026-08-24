from pages.base_page import BasePage


class CheckoutPage(BasePage):
    # Step one: customer info
    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"

    # Step two: order overview
    SUBTOTAL_LABEL = ".summary_subtotal_label"
    TAX_LABEL = ".summary_tax_label"
    TOTAL_LABEL = ".summary_total_label"
    FINISH_BUTTON = "#finish"

    # Step three: confirmation
    COMPLETE_HEADER = ".complete-header"

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.page.fill(self.FIRST_NAME_INPUT, first_name)
        self.page.fill(self.LAST_NAME_INPUT, last_name)
        self.page.fill(self.POSTAL_CODE_INPUT, postal_code)
        self.page.click(self.CONTINUE_BUTTON)

    def get_subtotal(self):
        text = self.page.locator(self.SUBTOTAL_LABEL).inner_text()
        return float(text.split("$")[-1])

    def get_tax(self):
        text = self.page.locator(self.TAX_LABEL).inner_text()
        return float(text.split("$")[-1])

    def get_total(self):
        text = self.page.locator(self.TOTAL_LABEL).inner_text()
        return float(text.split("$")[-1])

    def finish(self):
        self.page.click(self.FINISH_BUTTON)

    def get_confirmation_message(self):
        return self.page.locator(self.COMPLETE_HEADER).inner_text()
