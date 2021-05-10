import unittest
from tests.home.login_tests import Login_Tests
#from tests.green_kart.green_kart_csv_data import Green_Kart_csv_tests
from tests.green_kart.green_kart_tests import Green_Kart_tests

# Get all tests from the testcases
tc1 = unittest.TestLoader().loadTestsFromTestCase(Login_Tests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Green_Kart_tests)

#Create a test suite combining all the testcases
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner().run(smokeTest)

