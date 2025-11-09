import os
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait



def before_all(context):
    import yaml
    BS_HUB = "https://hub.browserstack.com/wd/hub"


    use_bs = os.getenv("BROWSERSTACK", "false").lower() == "true"

    if use_bs:
        # --- BrowserStack setup (read YAML, pick macOS Safari entry) ---
        with open("browserstack.yml", "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)

        user = os.getenv("BROWSERSTACK_USERNAME") or cfg.get("userName")
        key  = os.getenv("BROWSERSTACK_ACCESS_KEY") or cfg.get("accessKey")
        if not user or not key:
            raise RuntimeError("Missing BrowserStack credentials")

        mac = cfg["platforms"][1]  # OS X / Safari 15.6 entry

        bstack_opts = {
            "os":        mac["os"],
            "osVersion": str(mac["osVersion"]),
            "userName":  user,
            "accessKey": key,
            "projectName": cfg.get("projectName", "BrowserStack Sample"),
            "buildName":   cfg.get("buildName", "Safari Mac Run"),
        }

        from selenium.webdriver import SafariOptions
        options = SafariOptions()
        options.set_capability("browserName", mac["browserName"])             # "Safari"
        options.set_capability("browserVersion", str(mac["browserVersion"]))  # "15.6"
        options.set_capability("bstack:options", bstack_opts)

        context.driver = webdriver.Remote(command_executor=BS_HUB, options=options)

    else:

        browser  = os.getenv("BROWSER", "chrome").lower()   # chrome | firefox
        headless = os.getenv("HEADLESS", "1").lower() in ("1", "true", "yes")

        if browser == "mobile":
            device = os.getenv("DEVICE", "Pixel 2")

            opts = webdriver.ChromeOptions()
            opts.add_experimental_option("mobileEmulation", {"deviceName": device})

            if headless:
                opts.add_argument("--headless=new")
            context.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=opts
            )

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
