import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login import LoginPage
from selenium.webdriver.support import expected_conditions as EC

class Test_Login:

    def test_login(self, setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.Enter_Email("admin@yourstore.com")
        self.lp.Enter_Password("admin")
        self.lp.Click_Login()
        if self.driver.title == "Dashboard / nopCommerce administration":
            self.lp.Click_Logout()
            assert True
        else:
            assert False
