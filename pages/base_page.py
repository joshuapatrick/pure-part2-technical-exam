import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def step(self, name):
        return allure.step(name)

    def attach_screenshot(self, name="Screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )