"""
Collect all the locators from green_kart shopping page.
Create separate methods for each element and the action performed on that.
Create another method to call the required methods to execute the tests.
"""
import time

from base.basepage import BasePage
from utilities.util import Util

class GreenKartPage(BasePage, Util):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _project_selection1 = "//a[contains(text(),'Automation Practise - 1')]"
    _search_product = "search-keyword"
    _add_to_cart = "//div[@class='product-action']/button"
    _cart_icon = "//a[@class='cart-icon']"
    _proceed_to_checkout ="//button[contains(text(),'PROCEED TO CHECKOUT')]"
    # Traverse back to parent class to find the name of the product using xpath
    _product_name = "//div[@class='product-action']/button/parent::div/parent::div/h4"
    _product_list_gk = []
    _product_list_co = []
    _product_name_co = "//p[@class='product-name']"
    _promo_code = "promoCode"
    _promo_button = "promoBtn"
    _promo_result = "//span[contains(text(),'Code applied ..!')]"
    _before_coupon, _after_coupon = "", ""
    _total_after_discount = "discountAmt"
    _product_price = "//tr/td[5]/p"
    _total_amount = "totAmt"
    _place_order = ""

    def select_project(self):
        self.clickElement(self._project_selection1, locatorType='xpath')

    def verify_title(self):
        return self.verifyPageTitle("GreenKart - veg and fruits kart")

    def search_product(self, name):
        self.sendKeys(name, self._search_product, locatorType="class")

    def add_to_cart(self):
        time.sleep(3)
        buttons = self.getElementList(self._add_to_cart, locatorType="xpath")
        for button in buttons:
            self.clickElement(element=button)

    def product_names_selected(self):
        items = self.getElementList(self._product_name, locatorType="xpath")
        for item in items:
            self._product_list_gk.append(self.getText(element=item))

    def cart_button(self):
        self.clickElement(self._cart_icon, locatorType='xpath')

    def proceed_to_checkout_btn(self):
        self.clickElement(self._proceed_to_checkout, locatorType="xpath")

    def product_list_checkout_page(self):
        time.sleep(3)
        items = self.getElementList(self._product_name_co, locatorType="xpath")
        for item in items:
            self._product_list_co.append(self.getText(element=item))
        # Total amount Before applying the coupon
        self._before_coupon = self.getText(self._total_after_discount, locatorType="class")
        return self._before_coupon

    def product_price_check(self):
        amounts = self.getElementList(self._product_price, locatorType="xpath")
        sum = 0
        for amount in amounts:
            sum += int(self.getText(element=amount))
        return sum

    def promo_code(self, promo_code):
        self.sendKeys(promo_code, self._promo_code, locatorType="class")
        self.clickElement(self._promo_button, locatorType="class")

    def green_kart_page(self):
        self.select_project()
        self.verify_title()

    def go_to_cart(self):
        self.add_to_cart()
        self.product_names_selected()
        self.cart_button()
        self.proceed_to_checkout_btn()
        self.product_list_checkout_page()

    def verify_product_list(self):

        if self._product_list_gk == self._product_list_co:
            return True
        else:
            return False

    def verify_promo_code_success(self):
        # messageElement = self.waitForElement(self._promo_result, locatorType="xpath")
        # result =  self.isElementPresent(element=messageElement)
        # return result
        time.sleep(5)
        # To check if coupon was applied
        self._after_coupon = self.getText(self._total_after_discount, locatorType="class")
        if (self._after_coupon) != (self._before_coupon):
            return True
        else:
            return False

    def verify_total_amount(self):
        total_amount = self.getText(self._total_amount, locatorType='class')
        if self.product_price_check() == int(total_amount):
            return True
        else:
            return False




