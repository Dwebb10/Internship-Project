from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlsplit
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    EMAIL = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT = (By.CSS_SELECTOR, "a[wized='loginButton']")
    LOGGED_IN = (By.CSS_SELECTOR, "a[href='/secondary-listings']")

    def __init__(self, driver, wait):
        self.driver, self.wait = driver, wait

    def open(self, url):
        self.driver.get(url)

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.SUBMIT).click()

    def wait_until_logged_in(self):
        w = WebDriverWait(self.driver, 30)
        #self.wait.until(EC.presence_of_element_located(self.LOGGED_IN))


class Sidebar:

    SECONDARY = (
        By.CSS_SELECTOR,
        "a[href='/secondary-listings'], a[href='/secondary_listings']"
    )

    def __init__(self, driver, wait):
        self.driver, self.wait = driver, wait

    def click_secondary(self):

        try:
            el = self.wait.until(EC.element_to_be_clickable(self.SECONDARY))
            el.click()
            return
        except TimeoutException:
            pass


        parts = urlsplit(self.driver.current_url)
        origin = f"{parts.scheme}://{parts.netloc}"

        for path in ("/secondary_listings", "/secondary-listings"):
            self.driver.get(origin + path)
            try:
                self.wait.until(lambda d: "/secondary" in d.current_url.lower())
                return
            except Exception:
                continue




class SecondaryPage:
    NEXT = (By.CSS_SELECTOR, "a[wized='nextPageMLS']")
    PREV = (By.CSS_SELECTOR, "div[wized='previousPageMLS']")

    def __init__(self, driver, wait):
        self.driver, self.wait = driver, wait

    def assert_loaded(self):
        self.wait.until(lambda d: "/secondary" in d.current_url.lower())

    def go_last(self):
        for _ in range(155):
            try:
                self.wait.until(EC.element_to_be_clickable(self.NEXT)).click()
                time.sleep(1.5)
            except:
                break

    def go_first(self):
        for _ in range(155):
            try:
                self.wait.until(EC.element_to_be_clickable(self.PREV)).click()
                time.sleep(1.5)
            except:
                break


