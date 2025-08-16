from  selenium.webdriver.common.by import By

class SignUpPage:
    mobileNumber_xpath="//input[@id='ap_email_login']"
    continueBtn_xpath="//input[@type='submit']"
    createBtn_xpath="//span[@class='a-button-inner']"
    name_xpath="//input[@id='ap_customer_name']"
    password_xpath="//input[@id='ap_password']"
    verifyNumber_xpath="//input[@id='continue']"

    def __init__(self,driver):
        self.driver=driver

    def enterMobileNumber(self,mobile):
        self.driver.find_element(By.XPATH, self.mobileNumber_xpath).send_keys(mobile)

    def clickContinueButton(self):
        self.driver.find_element(By.XPATH, self.continueBtn_xpath).click()

    def clickCreateBtn(self):
        self.driver.find_element(By.XPATH, self.createBtn_xpath).click()

    def enterUserName(self, name):
        self.driver.find_element(By.XPATH, self.name_xpath).send_keys(name)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def clickVerifyNumberButton(self):
        self.driver.find_element(By.XPATH, self.verifyNumber_xpath).click()

