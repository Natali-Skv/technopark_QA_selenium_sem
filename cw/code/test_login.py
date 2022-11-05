import pytest
from ui.pages.base_page import BasePage
from ui.login_setup.base_case import BaseCase

class TestLogin(BaseCase):
    authorize = False

    def test_login(self, credentials):
        self.login_page.login(*credentials)
        assert str(self.driver.current_url) == 'https://target-sandbox.my.com/dashboard'
        assert self.base_page.find(BasePage.locators.USERNAME).get_attribute('title') == credentials[0]
