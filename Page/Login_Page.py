from selenium.webdriver.common.by import By
from Page.basic_page import Basic_page

class Login_page(Basic_page):
    username_loc = (By.XPATH, "//*[contains(@text,'請輸入登錄名稱')]")
    password_loc = (By.XPATH, "//*[contains(@text,'請輸入密碼')]")
    login_btn = (By.XPATH, "//*[contains(@text,'登入')]")

    def user_input(self,username):
        self.send_key(self.username_loc,username)

    def password_input(self,password):
        self.send_key(self.password_loc,password)

    def login_btn_input(self):
        self.click(self.login_btn)
