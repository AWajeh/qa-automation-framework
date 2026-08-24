"""Shared fixtures and hooks for the whole test suite.

The `page` fixture itself (browser launch, context, teardown) comes from the
pytest-playwright plugin — this file only adds project-specific fixtures and
the auto-screenshot-on-failure hook on top of it.
"""

import os
import allure
import pytest

from pages.login_page import LoginPage
from utils.test_data import VALID_USER

SCREENSHOT_DIR = "screenshots"


@pytest.fixture
def logged_in_page(page):
    """Returns a page that is already logged in as the standard valid user."""
    login_page = LoginPage(page).load()
    login_page.login(VALID_USER["username"], VALID_USER["password"])
    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take a screenshot and attach it to the Allure report on any test failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"{item.name}.png")
            page.screenshot(path=screenshot_path)
            allure.attach.file(
                screenshot_path,
                name="failure-screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
