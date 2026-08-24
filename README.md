# QA Automation Framework — SauceDemo

An end-to-end test automation framework built against [SauceDemo](https://www.saucedemo.com/), demonstrating a clean Page Object Model architecture, automatic failure screenshots, Allure reporting, and CI via GitHub Actions.

## Tech Stack

- **Python** + **Playwright** (sync API) — browser automation
- **PyTest** + **pytest-playwright** — test runner and browser fixtures
- **Allure Reports** — interactive HTML test reports
- **GitHub Actions** — CI, runs the suite on every push/PR

## Project Structure

```
qa-automation-framework/
├── .github/workflows/main.yml   CI pipeline
├── pages/                       Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── conftest.py              fixtures + auto-screenshot-on-failure hook
│   ├── test_login.py            valid / invalid / locked-out login
│   ├── test_cart.py             add-to-cart, price & item verification
│   └── test_checkout_e2e.py     full checkout flow (cart → payment → confirmation)
├── utils/test_data.py           test users, product slugs
├── requirements.txt
└── pytest.ini
```

## Scenarios Covered

- **Login:** valid credentials, wrong password, locked-out user
- **Cart:** adding items updates the cart badge; cart contents & prices match the product listing
- **Checkout (E2E):** add items → cart → shipping info → order summary (subtotal + tax = total) → confirmation
- **Failure handling:** any failing test automatically captures a screenshot and attaches it to the Allure report

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
playwright install chromium

pytest                # headless
pytest --headed       # watch the browser run
```

## View the Allure report

```bash
pip install allure-pytest      # already in requirements.txt
pytest                          # generates ./allure-results

# requires the Allure commandline tool (https://allurereport.org/docs/install/)
allure serve allure-results
```

## CI

Every push/PR to `main` runs the full suite headlessly on GitHub Actions (`.github/workflows/main.yml`) and uploads the Allure results and any failure screenshots as build artifacts.
