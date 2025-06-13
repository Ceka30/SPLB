import allure
from allure_commons.types import AttachmentType


def attach_screenshot(driver):
    screenshot = driver.get_screenshot_as_png()
    allure.attach(screenshot, name="screenshot", attachment_type=AttachmentType.PNG)
