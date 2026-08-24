"""Base class every page object inherits from — holds the shared Playwright page."""


class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def title(self):
        return self.page.title()
