import time
from utilities.webDriverUtility import WebDriverUtility
from locators.registerUserLocators import RegisterUserLocator
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

rul = RegisterUserLocator()

class RegisterUser():

    def __init__(self , driver):
        self.driver = driver
        self.util = WebDriverUtility(driver)
        self.waitObj = WebDriverWait(driver , 10)
        

    def enterFirstName(self , firstName):
        self.util.enterData(rul.firstName , firstName)

    def enterLastName(self , lastName):
        self.util.enterData(rul.lastName , lastName)

    def enterAddress(self , address):
        self.util.enterData(rul.address , address)

    def enterCity(self , city):
        self.util.enterData(rul.city , city)

    def enterState(self , state ):
        self.util.enterData(rul.state , state)

    def enterZipcode(self , zipcode ):
        self.util.enterData(rul.zipcode , zipcode)

    def enterPhoneNumber(self , phone ):
        self.util.enterData(rul.phone , phone)

    def enterSSN(self , ssn ):
        self.util.enterData(rul.ssn , ssn)

    def enterUsername(self , username):
        self.util.enterData(rul.username , username)

    def enterPassword(self , password):
        self.util.enterData(rul.password , password)

    def cnfrmPassword(self , password):
        self.util.enterData(rul.cnfrmPassword , password)

    def registerUser(self):
        self.util.click(rul.registerUser)


    def verifyRegistration(self):
        self.waitObj.until(ec.visibility_of_element_located(rul.verifyRegistration))
        time.sleep(10)
