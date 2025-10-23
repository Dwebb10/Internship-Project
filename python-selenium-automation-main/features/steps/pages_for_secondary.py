from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    EMAIL = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT = (By.CSS_SELECTOR, "a[wized='loginButton']")
    LOGGED_IN = (By.XPATH, "//div[normalize-space()='Secondary']/ancestor::a[1]")

    def __init__(self, driver, wait):
        self.driver, self.wait = driver, wait

    def open(self, url):
        self.driver.get(url)

    def login(self, user, pwd):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(user)
        self.driver.find_element(*self.PASSWORD).send_keys(pwd)
        self.driver.find_element(*self.SUBMIT).click()

    def wait_until_logged_in(self):
        self.wait.until(EC.presence_of_element_located(self.LOGGED_IN))


class Sidebar:
    SECONDARY = (By.XPATH, "//div[normalize-space()='Secondary']/ancestor::a[1]")

    def __init__(self, driver, wait):
        self.driver, self.wait = driver, wait

    def click_secondary(self):
        self.wait.until(EC.element_to_be_clickable(self.SECONDARY)).click()


class SecondaryPage:
    NEXT = (By.CSS_SELECTOR, "a[wized='nextPageMLS']")
    PREV = (By.CSS_SELECTOR, "div[wized='previousPageMLS']")

    def __init__(self, driver, wait):
        self.driver, self.wait = driver, wait

    def assert_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.NEXT))

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


