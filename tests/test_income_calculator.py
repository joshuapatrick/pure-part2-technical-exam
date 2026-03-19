import json
import pytest
import allure
from pages.income_calculator_page import IncomeCalculatorPage


def normalize_status(status):
    if "Qualified" in status:
        return "Qualified"
    elif "Conditions" in status:
        return "Conditional"
    elif "Not met" in status:
        return "Not met"


def load_data():
    with open("data/test_data.json") as f:
        return json.load(f)


@allure.feature("Income Calculator")
@allure.story("Valid and Invalid Scenarios")
@pytest.mark.parametrize("case", ["valid_case", "invalid_case"])
def test_income_calculation(driver, case):

    data = load_data()[case]

    page = IncomeCalculatorPage(driver)
    page.open()
    page.set_rent(data["rent"])
    page.set_income(data["income"])

    status = page.get_status()

    assert normalize_status(status) == data["expected"]