import allure
from playwright.sync_api import Page

from general.checkers.postgres_checkers import check_postgres_project_exists
from general.paths.ui_paths import ProjectPaths
from general.utils import make_url
from test_data.app_test_data import app_test_data


@allure.step('Test success create app valid data')
def test_ui_playwright_success_create_app_valid_data(
        page: Page, auth_user_ui, user_id, new_project, page_registry):
    request_body = app_test_data.create_valid_data()
    projects_page = page_registry.projects_page

    page.goto(make_url(ProjectPaths.GET_PROJECT, id=new_project[0]))
    projects_page.expect_project_page()

    with allure.step('User clicks create app button'):
        projects_page.create_app_button.click()
        projects_page.expect_skeleton_app_inputs()

    with allure.step('User enters app inputs'):
        projects_page.fill_app_inputs(**request_body)

    with allure.step('User clicks create app button'):
        projects_page.app_submit_button.click()

    projects_page.expect_app_card()

    check_postgres_project_exists(
        user_id=user_id,
        expected=True,
        project_id=new_project[0]
    )
