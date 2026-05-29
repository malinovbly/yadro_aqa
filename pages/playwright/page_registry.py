from pages.playwright.login_page import LoginPage
from pages.playwright.projects_page import ProjectsPage


class PageRegistry:
    def __init__(self, page):
        self.page = page

    @property
    def login_page(self):
        return LoginPage(self.page)

    @property
    def projects_page(self):
        return ProjectsPage(self.page)
