import time

from pageObjects.HomePage import HomePage
from pageObjects.SignUpPage import SignUpPage
from utilities.readProperties import ReadConfig


class Test_001_SignUpPage:
    baseURL=ReadConfig.getApplicationURL()

    def test_account_reg(self,setUp):
        self.driver=setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        # time.sleep(2)
        # self.hp.clickContinueButton()
        time.sleep(2)
        self.hp.clickAccountsList()
        time.sleep(2)
        self.hp.clickStartHere()

        self.sp=SignUpPage(self.driver)
        time.sleep(2)
        self.sp.enterMobileNumber(ReadConfig.getMobileNumber(self.driver))
        time.sleep(2)
        self.sp.clickContinueButton()
        time.sleep(2)
        self.sp.clickCreateBtn()
        time.sleep(2)
        self.sp.enterUserName(ReadConfig.getUserName(self.driver))
        time.sleep(2)
        self.sp.enterPassword(ReadConfig.getPassword(self.driver))
        time.sleep(2)
        self.sp.clickVerifyNumberButton()
