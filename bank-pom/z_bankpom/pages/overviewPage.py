import time
from utilities.webDriverUtility import WebDriverUtility
from locators.overviewLocators import OverviewLocators
from selenium.webdriver.support.select import Select

ol = OverviewLocators()


class OverviewPage():

    def __init__(self , driver):
        self.driver = driver
        self.util = WebDriverUtility(driver)

    def openNewAccountBtn(self):
        self.util.click(ol.openNewAccountBtn)
        time.sleep(1)

    def selectAccountType(self , texts):
        accountMode = self.driver.find_element(*ol.selectAccountType)
        accountSelect = Select(accountMode)
        accountSelect.select_by_visible_text(texts)
        time.sleep(1)

    def selectAccountNumber(self , texts):
        print(texts)


    def createNewAccountBtn(self):
        self.util.click(ol.createNewAccountbtn)


    def transferFundsBtn(self):
        self.util.click(ol.transferFundsBtn)