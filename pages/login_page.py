from pages.base_page import BasePage
from utils.test_data import BASE_URL


class LoginPage(BasePage):
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def load(self):
        self.goto(BASE_URL)
        return self

    def login(self, username, password):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.page.locator(self.ERROR_MESSAGE).inner_text()

    def is_error_visible(self):
        return self.page.locator(self.ERROR_MESSAGE).is_visible()
