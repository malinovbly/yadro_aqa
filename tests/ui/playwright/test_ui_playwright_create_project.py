import allure
import pytest
from playwright.sync_api import Page

from test_data.project_test_data import project_test_data


@pytest.mark.skip(reason='Currently has no project deletion after test & has not postgres check')
def test_ui_playwright_success_create_project_valid_data(
        page: Page, auth_user_ui, page_registry, project_cleanup):
    project_name = project_test_data.create_valid_data()['name']
    projects_page = page_registry.projects_page

    with allure.step('User clicks create project button'):
        try:
            projects_page.expect_has_projects()
            projects_page.not_empty_create_project_button.click()
        except AssertionError:
            projects_page.expect_no_projects()
            projects_page.empty_create_project_button.click()
        projects_page.expect_skeleton_project_inputs()

    with allure.step('User enters project name and submits'):
        projects_page.fill_project_inputs(name=project_name)
        projects_page.project_submit_button.click()
