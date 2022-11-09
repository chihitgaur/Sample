import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Nykaa_Locators.Homepagelocs import submit_button, item_clicked, add_button, search_box
from Nykaa_utilities.Login_here import Logging
from Nykaa_utilities.Searching_pdt import searchpdt
from Nykaa_utilities.Item_Cart import addtocart


class TestNykaaAutomate():

    @pytest.mark.usefixtures("initiate_driver")
    def test_perform_logging_in(self, initiate_driver):
        driver = initiate_driver

        Logging().perform_login(submit_button)
        assert driver.find_elements(by=By.XPATH, value=search_box), "Wrong Otp"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_button)))


    @pytest.mark.parametrize('entr_mobile',
                                 [("8076042540"), ("98765431"), (""), ("123456789")])
    def test_login_function_with_invalid_details(self, initiate_driver,entr_mobile):
            Logging().perform_login(entr_mobile)

            b=initiate_driver.find_element(by=By.XPATH,value=search_box).txt
            assert b == "Please enter a valid mobile number!"



    def test_placing_order_after_loggging(self, initiate_driver):
        driver=initiate_driver
        Logging().perform_login(submit_button)
        assert driver.find_elements(by=By.XPATH, value=search_box), "Wrong Otp"

        searchpdt().item_to_clicked(item_clicked)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,item_clicked )))
        addtocart().switching_tabs(1)
        addtocart().addin_to_cart(add_button)
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, add_button)))



