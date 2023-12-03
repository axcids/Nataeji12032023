import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="--browser_name: chrome, firefox, edge"
    )


@pytest.fixture(scope="class")
def setup(request):
    
    browser_name = request.config.getoption("browser_name")
    
    if browser_name == "chrome":
        service_obj = Service(r"C:\webdrivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(10)
        
    elif browser_name == "firefox":
        # write the code for firefox browser invocation
        pass
    elif browser_name == "edge":
        # write the code for edge browser invocation
        pass
    
    driver.get("https://exam-stg-web.moe.gov.sa/")
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
