from playwright.sync_api import expect

from pages.playwright.base_page import BasePage


class ProjectsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    #region locators
    @property
    def projects_title(self):
        return self.page.locator('//div[@class="header__title"]')

    @property
    def empty_title(self):
        return self.page.locator('//div[@class="empty__title"]')

    @property
    def not_empty_create_project_button(self):
        return self.projects_title.locator('//..//button[@type="button"]')

    @property
    def empty_create_project_button(self):
        return self.page.locator('//div[@class="t-block-actions"]//button[@type="button"]')

    @property
    def project_name_input(self):
        return self.page.locator('//input[@formcontrolname="name"]')

    @property
    def project_submit_button(self):
        return self.page.locator('//div[@class="controls"]//button[@data-appearance="primary"]')

    @property
    def project_item_info(self):
        return self.page.locator('//app-project-item')

    @property
    def create_app_button(self):
        return self.page.locator('//div[@class="app-new__icon"]')

    @property
    def app_name_input(self):
        return self.page.locator('//input[@formcontrolname="name"]')

    @property
    def package_name_input(self):
        return self.page.locator('//input[@formcontrolname="package_name"]')

    @property
    def app_signature_input(self):
        return self.page.locator('//textarea[@formcontrolname="app_signature"]')

    @property
    def app_submit_button(self):
        return self.page.locator('//button[@type="submit"]')

    @property
    def app_icon(self):
        return self.page.locator('//img[@alt="android"]')
    #endregion

    #region actions
    def fill_project_inputs(self, name):
        self.project_name_input.fill(name)

    def fill_app_inputs(self, name, package_name, app_signature):
        self.app_name_input.fill(name)
        self.package_name_input.fill(package_name)
        self.app_signature_input.fill(app_signature)
    #endregion

    #region expectations
    def expect_has_projects(self):
        expect(self.projects_title).to_be_visible(timeout=1000)

    def expect_no_projects(self):
        expect(self.empty_title).to_be_visible()

    def expect_project_page(self):
        expect(self.project_item_info).to_be_visible()

    def expect_skeleton_project_inputs(self):
        expect(self.project_name_input).to_be_visible()
        expect(self.project_submit_button).to_be_enabled()

    def expect_skeleton_app_inputs(self):
        expect(self.app_name_input).to_be_visible()
        expect(self.package_name_input).to_be_visible()
        expect(self.app_signature_input).to_be_visible()
        expect(self.app_submit_button).to_be_enabled()

    def expect_app_card(self):
        expect(self.app_icon).to_be_visible()
    #endregion
