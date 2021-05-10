import time
import pytest
from pages.green_kart.green_kart_page import GreenKartPage
from utilities.teststatus import TestStatus
import unittest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt
class Green_Kart_tests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, oneTimeSetUp):
        self.gp = GreenKartPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("ber", "rahulshettyacademy"))
    @unpack
    def test_gk_shopping_page(self, search_item, promo_code):
        self.gp.green_kart_page()
        time.sleep(3)
        result1 = self.gp.verify_title()
        # Assert result and mark in the list
        self.ts.mark(result1, "Title is incorrect")

        # To test Search
        self.gp.search_product(search_item)

        # To test add to cart
        time.sleep(3)
        self.gp.go_to_cart()
        result2 = self.gp.verify_product_list()
        self.ts.mark(result2,"Count mismatch")

    # @pytest.mark.run(order=2)
    # @data("rahulshettyacademy")
    # @unpack
    # def test_promo_code(self, promo_code):
        #To test promo code
        self.gp.promo_code(promo_code)
        result3 = self.gp.verify_promo_code_success()
        self.ts.mark(result3, "Promo code invalid")

    @pytest.mark.run(order=3)
    def test_total_amount(self):
        result4 = self.gp.verify_total_amount()
        self.ts.markFinal("Total amount matched", result4, "Total amount not equal")
        