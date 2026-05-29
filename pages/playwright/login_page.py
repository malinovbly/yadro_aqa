from playwright.sync_api import expect

from pages.playwright.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    #region locators
    @property
    def email_input(self):
        return self.page.locator('form div tui-textfield input[formcontrolname="email"]')

    @property
    def password_input(self):
        return self.page.locator('//input[@formcontrolname="password"]')

    @property
    def submit_button(self):
        return self.page.locator('//button[@type="submit"]')
    #endregion

    #region actions
    def fill_inputs(self, user_data):
        self.email_input.fill(user_data['email'])
        self.password_input.fill(user_data['password'])
    #endregion

    #region expectations
    def expect_skeleton(self):
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.submit_button).to_be_enabled()

    def expect_filled(self, user_data):
        expect(self.email_input).to_have_value(user_data['email'])
        expect(self.password_input).to_have_value(user_data['password'])
        expect(self.submit_button).to_be_enabled()
    #endregion
