import time
from selenium.webdriver.common.by import By


from Nykaa_Locators.Homepagelocs import account_button, ls_button, enter_no, Verify_button
from Nykaa_Locators.loginpagelocs import phone_no
from conftest import driver


class Logging():
    def click_acct(self, account_button ):

        driver.find_element(by=By.XPATH, value=account_button).click()

    def enter_no(self, phone_no):
        self.click_acct(account_button)

        driver.find_element(by=By.XPATH, value=ls_button).click()

        driver.find_element(by=By.XPATH, value=enter_no).send_keys(phone_no)

    def perform_login(self, submit_button):
        self.enter_no(phone_no)

        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Verify_button)))
        driver.find_element(by=By.XPATH, value=submit_button).click()
        time.sleep(10)
        driver.find_element(by=By.XPATH,value=Verify_button).click()
