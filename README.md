# Selenium Pytest Automation Framework

A scalable and maintainable test automation framework built using **Python**, **Selenium WebDriver**, and **Pytest**, following the **Page Object Model (POM)** design pattern with **Allure Reporting** integration.

---

## Project Overview

This framework demonstrates a clean and professional automation setup with:

* Page Object Model (POM)
* Centralized test setup using `conftest.py`
* Built-in Selenium driver management (no manual drivers required)
* Allure reporting with step-level logging and screenshots
* Data-driven testing using JSON
* Reusable utilities and clean architecture

---

## Project Structure

```
pure_part2_technical_exam/
│
├── data/
│   └── test_data.json
│
├── pages/
│   ├── base_page.py
│   └── income_calculator_page.py
│
├── tests/
│   └── test_income_calculator.py
│
├── utils/
│   ├── driver_factory.py
│   └── waits.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Tech Stack

* **Python 3.x**
* **Selenium WebDriver (built-in driver manager)**
* **Pytest**
* **Allure Reports**
* **JSON (Test Data)**

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd pure_part2_technical_exam
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Tests

```bash
pytest
```

---

## Allure Reporting

### Generate and view report:

```bash
allure serve allure-results
```

---

### Features:

* Step-by-step execution logs
* Screenshot captured on each action
* Automatic screenshot on failure
* Clean and interactive UI

---

## Test Design

### Page Object Model (POM)

Encapsulates:

* Locators
* Actions
* Allure steps
* Screenshot attachments

---

### `conftest.py`

Centralized configuration for:

* WebDriver setup and teardown
* Allure hooks (e.g., screenshot on failure)
* Test lifecycle management

---

### Data-Driven Testing

```python
@pytest.mark.parametrize("case", ["valid_case", "invalid_case"])
```

Test data is stored in:

```
data/test_data.json
```

---

## Best Practices Used

* Separation of concerns (Test vs Page vs Setup)
* Reusable utilities
* No hardcoded waits (uses explicit waits)
* No driver binaries committed
* Clean reporting integration

---

## Future Improvements

* Cross-browser support (Chrome, Firefox)
* Headless execution
* Parallel test execution (`pytest-xdist`)
* CI/CD integration (GitHub Actions)
* Test tagging (smoke, regression)

---

## Author

**Joshua Patrick**

Senior QA Automation Engineer (Cypress | Robot Framework | Selenium)

---

## License

This project is for demonstration and assessment purposes.
