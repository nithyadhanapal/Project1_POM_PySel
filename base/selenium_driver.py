import os
import time
import traceback

from selenium.webdriver.common.by import By
from traceback import print_stack

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging


class SeleniumDriver:

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'class':
            return By.CLASS_NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'tag':
            return By.TAG_NAME
        elif locatorType == 'link':
            return By.LINK_TEXT
        elif locatorType == "partial_link":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info("Locator Type" + locatorType + "is not supported/correct.")
        return False

    def getTitle(self):
        return self.driver.title

    def getElement(self, locator, locatorType='id'):
        """
        To fine element
        :param locator:
        :param locatorType:
        :return:
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            self.log.info("Element Found with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Element Not Found with locator: " + locator + " locatorType: " + locatorType)
        return element

    def getElementList(self, locator, locatorType='id'):
        """
        To get list of elements
        :param locator:
        :param locatorType:
        :return: list
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType,locator)
            self.log.info("Element Found with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Element Not Found with locator: " + locator + " locatorType: " + locatorType)
        return element

    def clickElement(self, locator="", locatorType="id", element = None):
        """
        Click on an element.
        Either provide element or combination of locator and locatorType
        :param locator:
        :param locatorType:
        :return:
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " , locator , " locatorType: " , locatorType)
        except:
            print("Cannot click on the element with locator: " , locator , " locatorType: " , locatorType)
            print_stack()

    def sendKeys(self, data, locator="", locatorType='id', element = None):
        """
        To send data to a field
        Either provide element or combination of locator and locatorType
        :param data:
        :param locator:
        :param locatorType:
        :return:
        """
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator="", locatorType='id', element = None):
        """
        To check if the element is present in the page
        :param locator:
        :param locatorType:
        :return:
        """
        try:
            if locator:
                element = self.driver.find_element(locatorType, locator)
            if element is not None:
                self.log.info("Element Present with locator: " + locator + " locatorType: " + locatorType)
                return True
        except:
            self.log.info("Element not present with locator: " + locator + " locatorType: " + locatorType)
            return False

    def isElementDisplayed(self, locator="", locatorType='id', element = None):
        """
        To check if the element is present in the page
        :param locator:
        :param locatorType:
        :return:
        """
        isDisplayed = False
        try:
            if locator:
                element = self.driver.find_element(locatorType, locator)
            if element is not None:
                self.log.info("Element is displayed with locator: " + locator + " locatorType: " + locatorType)
            return isDisplayed
        except:
            self.log.info("Element not displayed with locator: " + locator + " locatorType: " + locatorType)
            return False

    def AreElementsPresent(self, locator, locatorType):
        """
        To check if there are list of elements present
        :param locator:
        :param locatorType:
        :return:
        """
        try:
            element = self.driver.find_elements(locatorType, locator)
            if len(element) > 0:
                self.log.info("Elements Present with locator: " + locator + " locatorType: " + locatorType)
                return True
        except:
            self.log.info("Elements not present with locator: " + locator + " locatorType: " + locatorType)
            return False

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator: # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def clearField(self, locator, locatorType="id"):
        """
        To clear the field before sending data
        :param locator:
        :param locatorType:
        :return:
        """
        try:
            element = self.getElement(locator, locatorType="id")
            element.clear()
            self.log.info("Cleared field with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Cannot clear text field with locator: " + locator + " and  locatorType: " + locatorType)

    def waitImplicitly(self, timeSec):
        """
        To implicitly wait for the page to load
        :return:
        """
        return self.driver.implicitly_wait(timeSec)

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        """
        To explicitly wait for the element to load
        :param locator:
        :param locatorType:
        :param timeout:
        :param pollFrequency:
        :return:
        """
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable/present")
            wait = WebDriverWait(self.driver, timeout=15, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def screenShot(self,testMessage):
        """
        Take screenshot of the current open web page
        :param testMessage:
        :return:
        """
        fileName = testMessage + '.' + str(round(time.time() * 1000)) + '.png'
        screenshotDirectory = '../screenshots/'
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory,relativeFileName)
        destinationDirectory = os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot saved to directory" + destinationFile)
        except:
            self.log.error("### EXCEPTION OCCURRED")
            print_stack()

    def wedScroll(self, direction = 'up'):
        """
        Function to scroll up/down in a web page
        :param direction:
        :return:
        """
        # Scroll Up
        if direction == 'up':
            self.driver.execute_script("window.scrollBy(0,1000);")
        # Scroll Down
        if direction == 'down':
            self.driver.execute_script("window.scrollBy(0,-1000);")

    def SwitchFrameByIndex(self, locator, locatorType="xpath"):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", locatorType="xpath")
            self.log.info("Length of iframe list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                result = self.isElementPresent(locator, locatorType)
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            print("iFrame index not found")
            return result

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):
        """
        Switch to default content

        Parameters:
            None
        Returns:
            None
        Exception:
            None
        """
        self.driver.switch_to.default_content()

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    def selectDropdown(self, dropDownElement=None, info="",
                       byValue=False, byIndex=False, byVisibleText=False, locator="", locatorType="id", timeToWait=0):
        """
        Select option from a dropdown (default by visible text)

        Parameters:
            1. Required:
                None
            2. Optional:
                1. dropDownElement - Dropdown element
                2. info            - Information about the optionToSelect, usually text on the optionToSelect
                3. byValue         - Provide True if you want to select by Value
                4. byIndex         - Provide True if you want to select by index
                5. byVisibleText   - Provide True if you want to select by Visible text
                6. locator         - Locator of the element to check
                7. locatorType     - Type of the locator(id(default), xpath, css, className, linkText)
                8. timeToWait      - Time you want to wait after selecting the element
        Returns:
            None
        Exception:
            None
        """
        if locator:
            dropDownElement = self.getElement(locator, locatorType=locatorType)
        if dropDownElement is not None:
            try:
                select = Select(dropDownElement)
                if byValue:
                    select.select_by_value(byValue)
                    print("Selected by value: " + str(byValue))
                elif byIndex:
                    select.select_by_index(byIndex)
                    print("Selected by index: " + str(byIndex))
                else:
                    select.select_by_visible_text(byVisibleText)
                    print("Selected by Visible text: " + str(byVisibleText))
                # print("Selected option --> :: '" + optionToSelect + "' from dropdown:: '" + info + "'")
                print("Waiting after selecting the element for " + str(timeToWait) + " seconds")
                time.sleep(timeToWait)
            except:
                print("'Could not select option from dropdown" + info + "'")
                print("Exception Caught: {}".format(traceback.format_exc()))
                print("".join(traceback.format_stack()))