# features/tests/environment.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
    options = webdriver.ChromeOptions()


    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    context.driver.set_window_size(1400, 900)


    context.wait = WebDriverWait(context.driver, 15)

def after_all(context):
    context.driver.quit()
