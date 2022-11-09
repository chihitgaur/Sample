from selenium.webdriver.common.by import By

from Nykaa_Config.Configfile import pincode, adrrl1, adrrl2, name
from Nykaa_Locators.Homepagelocs import cart, pinc, adl1, adl2, nm
from conftest import driver

class proceeding():
    def going_to_cart(self,checkout):
        driver.switchTo().frame("/v2/checkout/?platform=desktop")
        driver.find_element(by=By.XPATH,value=cart).click()
        driver.find_element(by=By.XPATH,value=checkout).click()

    def adding_addr(self):
        driver.find_element(by=By.XPATH, value=pinc).send_keys(pincode)
        driver.find_element(by=By.XPATH, value=adl1).send_keys(adrrl1)
        driver.find_element(by=By.XPATH, value=adl2).send_keys(adrrl2)
        driver.find_element(by=By.XPATH, value=nm).send_keys(name)