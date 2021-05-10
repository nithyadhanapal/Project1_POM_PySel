"""
Collect all the locators from login page.
Create separate methods for each element and the action performed on that.
Create another method to call the required methods to execute the tests.

"""

from base.basepage import BasePage

class Login_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _practice_project_link = "//a[contains(text(),'Practice Projects')]"
    _username_field = "name"
    _email_field = "email"
    _check_terms = "agreeTerms"
    _submit_form = "form-submit"
    _page_validation = "//a[contains(text(),'Automation Practise - 1')]"

    def clickPracticePage(self):
        self.clickElement(self._practice_project_link, locatorType="xpath")

    def sendUserName(self, username):
        self.sendKeys(username,self._username_field)

    def sendEmail(self,email):
        self.sendKeys(email,self._email_field)

    def clickTerms(self):
        self.clickElement(self._check_terms )

    def clickSubmitForms(self):
        self.clickElement(self._submit_form)

    def login(self, username="", email=""):
        self.clickPracticePage()
        self.sendUserName(username)
        self.sendEmail(email)
        self.clickTerms()
        self.clickSubmitForms()

    def verifyLoginSuccess(self):
        result = self.isElementPresent(self._page_validation,locatorType="xpath")
        return result

    def verifyTitle(self):
        return self.verifyPageTitle("Rahul Shetty Academy")
