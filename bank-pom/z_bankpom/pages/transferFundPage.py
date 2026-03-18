import time
from locators.transferFundLocators import TransferFundLocators
from utilities.webDriverUtility import WebDriverUtility
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

tfl = TransferFundLocators()

class TransferFundsPage():

    def __init__(self , driver):
        self.driver = driver
        self.util = WebDriverUtility(driver)
        self.waitObj = WebDriverWait(driver , 10)
        

    def enterTransformAmount(self , transferAmount):
        self.util.enterData(tfl.enterTransferAmount , transferAmount)

    def selectFromAccount(self , texts):
        fromAccountMode = self.driver.find_element(*tfl.selectFromAccount)
        fromAccountSelect = Select(fromAccountMode)
        fromAccountSelect.select_by_visible_text(texts)
        

    def selectToAccount(self , texts):
        toAccountMode = self.driver.find_element(*tfl.selectToAccount)
        toAccountSelect = Select(toAccountMode)
        toAccountSelect.select_by_visible_text(texts)
        

    def clickTransferBtn(self):
        self.util.click(tfl.transferBtn)


    def verifyTransfer(self):
        self.waitObj.until(ec.visibility_of_element_located(tfl.verifyTransfer))
        time.sleep(2)

    def clickLogoutBtn(self):
        self.util.click(tfl.logOutButton)