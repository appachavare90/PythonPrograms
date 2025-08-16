from selenium.webdriver.common.by import By

class HomePage:
    accountList_xpath = "//button[contains(@aria-label,'Expand Account and Lists')]"
    sign_xpath = "//span[@class='nav-action-inner']"
    register_xpath = "//div[@id='nav-flyout-ya-newCust']/a"
    continueBtn="//button[@class='a-button-text']"

    def __init__(self, driver):
        self.driver = driver

    def clickAccountsList(self):
        self.driver.find_element(By.XPATH, self.accountList_xpath).click()

    def clickSignButton(self):
        self.driver.find_element(By.XPATH, self.sign_xpath).click()

    def clickStartHere(self):
        self.driver.find_element(By.XPATH, self.register_xpath).click()

    def clickContinueButton(self):
        self.driver.find_element(By.XPATH,self.continueBtn).click()


