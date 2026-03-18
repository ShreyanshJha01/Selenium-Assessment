class WebDriverUtility:

    def __init__(self , driver):
        self.driver = driver

    def click(self  , var):
        self.driver.find_element(*var).click()

    def enterData(self , var , data):
        self.driver.find_element(*var).send_keys(data)
        