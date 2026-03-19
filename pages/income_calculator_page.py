from selenium.webdriver.common.by import By
from utils.waits import wait_for_visible
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class IncomeCalculatorPage(BasePage):
    URL = "https://incomecalculator.purepm.dev"

    RENT_INPUT = (By.XPATH, "//label[contains(text(),'Rental Rate')]/following::input[1]")
    INCOME_INPUT = (By.XPATH, "//label[contains(text(),'Income Source')]/following::input[1]")
    STATUS = (By.XPATH, "//h2//span[contains(@class,'font-medium')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        with self.step("Open Income Calculator page"):
            self.driver.get(self.URL)
            self.attach_screenshot("Page Loaded")

    def set_rent(self, value):
        with self.step(f"Set rent: {value}"):
            el = wait_for_visible(self.driver, self.RENT_INPUT)
            el.clear()
            el.send_keys(value)
            self.attach_screenshot("Rent Entered")

    def set_income(self, value):
        with self.step(f"Set income: {value}"):
            el = wait_for_visible(self.driver, self.INCOME_INPUT)
            el.clear()
            el.send_keys(value)
            el.send_keys(Keys.TAB)  # triggers calculation
            self.attach_screenshot("Income Entered")

    def get_status(self):
        with self.step("Get result status"):
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.STATUS)
            )
            status = element.text.strip()
            self.attach_screenshot("Result Displayed")
            return status