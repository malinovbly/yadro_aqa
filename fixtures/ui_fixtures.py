import allure
import pytest

from config import BASE_URL
from pages.playwright.page_registry import PageRegistry


@pytest.fixture(scope='function')
def page_registry(page):
    return PageRegistry(page)


@pytest.fixture(scope='function')
def auth_user_ui(valid_user_data, page_registry):
    with allure.step('User opens Login page'):
        page_registry.login_page.open(BASE_URL)
        page_registry.login_page.expect_skeleton()

    with allure.step('User enters credentials'):
        page_registry.login_page.fill_inputs(valid_user_data)
        page_registry.login_page.expect_filled(valid_user_data)

    page_registry.login_page.submit_button.click()
