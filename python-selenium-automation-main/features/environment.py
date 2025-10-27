
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
    browser  = os.getenv("BROWSER", "firefox").lower()   # chrome | firefox
    headless = os.getenv("HEADLESS", "1").lower() in ("1", "true", "yes")

    if browser == "firefox":
        opts = webdriver.FirefoxOptions()
        if headless:
            opts.add_argument("--headless")
        context.driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=opts
        )
    else:  # chrome by default
        opts = webdriver.ChromeOptions()
        if headless:
            opts.add_argument("--headless=new")
        opts.add_argument("--window-size=1400,900")
        context.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=opts
        )

    context.wait = WebDriverWait(context.driver, 15)

def after_all(context):
    # be safe if before_all failed
    if getattr(context, "driver", None):
        context.driver.quit()


