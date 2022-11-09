from selenium.webdriver.common.by import By


from Nykaa_Locators.Homepagelocs import size_click, item
from conftest import driver


class addtocart():
    def click_on_pdt(self, item):
        driver.find_element(by=By.XPATH, value=item).click()

    def switching_tabs(self, num):
        self.click_on_pdt(item)
        tabs = driver.window_handles
        driver.switch_to.window(tabs[num])

    def addin_to_cart(self, add_button):

        driver.find_element(by=By.XPATH, value=size_click).click()

        driver.find_element(by=By.XPATH, value=add_button).click()
