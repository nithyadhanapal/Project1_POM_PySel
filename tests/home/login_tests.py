import time
import pytest
from pages.home.login_page import Login_Page
from utilities.teststatus import TestStatus
import unittest

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class Login_Tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.lp = Login_Page(self.driver)
        self.ts = TestStatus(self.driver)

    """
    Need to verify 2 verification points.
    If 1 fails, code will not go to the other point.
    If assert failes, it stops the current test execution and
    moves to the next test method
    """
    @pytest.mark.run(order=1)
    def test_validate_login(self):
        self.lp.login("Nithya dhanapal","nithyadhanapal@yahoo.com")
        time.sleep(3)
        result1 = self.lp.verifyTitle()
        #Assert result1 and mark in the list
        self.ts.mark(result1, "Title is incorrect")
        result2 = self.lp.verifyLoginSuccess()
        # Assert the last statement and append it to the final mark list
        self.ts.markFinal("Test_valid Login" , result2, "Login was not successful")






