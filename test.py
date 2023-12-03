import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service(r"C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://nataeji.moe.gov.sa/")

loginPage = driver.find_element(By.CLASS_NAME, "loginBtn").click()
loginByMadrasati = driver.find_element(By.XPATH, "//*[@id='loginModal']/div/div/div/div/div[5]/button").click()
time.sleep(5)

driver.close()
driver.quit()
