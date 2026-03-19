from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver_path = ChromeDriverManager().install()

    # 🔥 FIX: force correct executable
    if "chromedriver.exe" not in driver_path:
        driver_path = os.path.join(os.path.dirname(driver_path), "chromedriver.exe")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    return driver