# Import Tools
from selenium.webdriver.common.by import By
import pytest
import time
# Import Utilities
from Utilities.BaseClass import BaseClass
# Import Locators
from Locators.HomePageLocators import HomePageLocators
# Import Pages
from Pages.HomePage import HomePage



class Test_Home_Page_Elements(BaseClass):
    
    def test_case_1_check_elements_presence(self):
        
        # Assert Login Modal Button
        assert self.is_element_present(By.XPATH, HomePageLocators.button_for_login_options_modal), "Login modal button is not presented"
        # Assert Logo Button 
        assert self.is_element_present(By.XPATH, HomePageLocators.image_for_nataeji_logo), "Logo's hyperlink is not presented"
        