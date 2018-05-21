from time import sleep
from Page.basic_page import *
from Page.Login_Page import Login_page
from TestCase.basic_unittest import *
import unittest

class LoginTest(basic_unittest):
    def setUp(self):
        self.driver.launch_app()

    def test_login(self):
        ins_login = Login_page(self.driver)
        ins_login.user_input("test2018")
        ins_login.password_input("a12345678")
        ins_login.login_btn_input()

    def test_login2(self):
        ins_login = Login_page(self.driver)
        ins_login.user_input("test2018")
        ins_login.password_input("a12345678")
        ins_login.login_btn_input()

    def tearDown(self):
        self.driver.close_app()

# if __name__ =="__main__":
#     testsuit = unittest.TestSuite()
#     testsuit.addTest(LoginTest("test_login"))
#     testsuit.addTest(LoginTest("test_login2"))


