import pytest
import allure
import os
import shutil
from utils.driver_factory import get_driver


# ✅ Auto-clean Allure results before test run
def pytest_sessionstart(session):
    results_dir = "allure-results"

    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)

    os.makedirs(results_dir, exist_ok=True)


# ✅ Shared WebDriver fixture
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


# ✅ Screenshot on failure (automatic)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )