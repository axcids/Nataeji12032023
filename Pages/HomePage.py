# Import Tools
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# Import Utilities
from Utilities.BaseClass import BaseClass
# Import Pages
from Locators.HomePageLocators import HomePageLocators
from Pages.MicrosoftLoginPage import MicrosoftLoginPage 
from Pages.TechnicalSupportPage import TechnicalSupportPage



class HomePage(BaseClass):
        
    def __init__(self, driver):
        self.driver = driver
        
    # Header
    
    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, HomePageLocators.button_for_login_options_modal).click()  
    
    def click_on_account_settings(Self):
        pass
    
    def click_on_logout_button(self):
        self.driver.find_element(By.XPATH, HomePageLocators.button_for_logout).click()
        
    def is_logout_button_present(self):
        element_present = self.is_element_present(By.XPATH, HomePageLocators.button_for_logout)
        return element_present
    
    def click_to_open_microsoft_login_page(self):
        self.driver.find_element(By.XPATH, HomePageLocators.button_for_login_using_madrasati).click()
        pageObject = MicrosoftLoginPage(self.driver)
        return pageObject  

    # Body
    

    

    # Footer
    
    def click_to_open_technical_support_link(self):
        self.driver.find_element(By.XPATH, HomePageLocators.link_for_technical_support_page).click()
        pageObject = TechnicalSupportPage(self.driver)
        return pageObject
    
    def click_on_terms_and_conditions_link(self):
        pass
    
    def click_on_privacy_link(self):
        pass