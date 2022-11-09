import time
from selenium.webdriver.common.by import By

from Nykaa_Config.Configfile import Searchh
from Nykaa_Locators.Homepagelocs import search_box, item_clicked
from conftest import driver

class searchpdt():

    def searching_of_product(self, search_box):

        a=driver.find_element(by=By.XPATH,value=search_box)

        a.send_keys(Searchh)

    def item_to_clicked(self,item_clicked):

        self.searching_of_product(search_box)

        driver.find_element(by=By.XPATH,value=item_clicked).click()
