from Utilities.BaseClass import BaseClass
from Pages.HomePage import HomePage
import pytest
import time



class Test_Login_Options (BaseClass): 
    
    @pytest.fixture(params=[("T4eduTestStud139@nthb.moe.gov.sa", "TPwd@9090%#!@"),])
    def madrasati_login_data(self, request):
        return request.param
    
    def test_case_1_login_by_madrasati(self, madrasati_login_data):
        # Create instances of the pages 
        homePage = HomePage(self.driver)
        # Home Page Steps
        homePage.click_on_login_button()
        loginByMadrasati = homePage.click_to_open_microsoft_login_page()
        # Microsoft Login Steps
        loginByMadrasati.enter_email(madrasati_login_data[0])
        loginByMadrasati.click_next_to_password_page()
        loginByMadrasati.enter_password(madrasati_login_data[1])
        loginByMadrasati.click_login_button()
        # Check if the stay signed in option presented or not
        if loginByMadrasati.is_stay_signed_in_present :
            # Click yes to pass the page 
            loginByMadrasati.agree_on_stay_signed_in()
        
        time.sleep(10)
        # Assertions:
        # Check if the user have been transferred to the home page again 
        assert self.driver.current_url == "https://exam-stg-web.moe.gov.sa/home", "User did not transferred to home page again after login"
        # check if the user is actullay logged in by making sure logout button is present 
        assert homePage.is_logout_button_present, "Logout button is missing on home page which could mean the login process is not completed successfully"

        # homePage.click_on_logout_button()
        
    def test_case_2_login_by_nafath(self):
        pass
