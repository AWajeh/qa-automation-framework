"""Shared test data for SauceDemo tests."""

BASE_URL = "https://www.saucedemo.com/"

VALID_USER = {"username": "standard_user", "password": "secret_sauce"}
LOCKED_OUT_USER = {"username": "locked_out_user", "password": "secret_sauce"}
INVALID_USER = {"username": "standard_user", "password": "wrong_password"}

CHECKOUT_INFO = {"first_name": "Wajeh", "last_name": "QA", "postal_code": "12345"}

BACKPACK = "sauce-labs-backpack"
BIKE_LIGHT = "sauce-labs-bike-light"
