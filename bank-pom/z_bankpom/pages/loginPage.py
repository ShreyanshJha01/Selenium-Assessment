import time
from utilities.webDriverUtility import WebDriverUtility
from locators.loginLocators import LoginLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

ll = LoginLocators()

class LoginPage():

    def __init__(self , driver):
        self.driver = driver
        self.util = WebDriverUtility(driver)
        self.waitObj = WebDriverWait(driver , 10)

    def registerUser(self):
        self.util.click(ll.registerUser)

    def enterUsername(self , username):
        self.util.enterData(ll.username , username)

    def enterPassword(self , password):
        self.util.enterData(ll.password , password)

    def login(self):
        self.util.click(ll.login)
        self.waitObj.until(ec.visibility_of_element_located(ll.verifyLogin))
        time.sleep(1)

    
