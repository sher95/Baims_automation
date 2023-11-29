from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from allure_commons.types import AttachmentType
import time
import allure


class BasePage:
    """Base class"""

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def _wait_for_element(self, locator_val, locator_type, condition=EC.visibility_of_element_located):
        """Explicitly wait for an element to be present"""
        try:
            locator_type = locator_type.lower()
            wait = WebDriverWait(self.driver, 15, poll_frequency=1)
            element = wait.until(condition((getattr(By, locator_type.upper()), locator_val)))
            return element
        except NoSuchElementException:
            self.take_screenshot(f"ElementTimeout_{locator_val}")
            raise NoSuchElementException(f"Element not found: {locator_val}")

    def _perform_action(self, action, locator_val, locator_type="id", *args, **kwargs):
        """Perform common actions like click, send text, etc."""
        element = self._wait_for_element(locator_val, locator_type)
        action(element, *args, **kwargs)

    def get_element(self, locator_val, locator_type="id"):
        """Get element with optional wait time"""
        locator_type = locator_type.lower()
        return self._wait_for_element(locator_val, locator_type)

    def click_element(self, locator_val, locator_type="id"):
        """Click element with optional wait time"""
        self._perform_action(lambda e: e.click(), locator_val, locator_type)

    def click_element_by_text(self, text, locator_type="xpath"):
        """Click element by text"""
        locator = f"//*[text()='{text}']"
        self.click_element(locator, locator_type)

    def send_text(self, text, locator_val, locator_type="id"):
        """Send text with optional wait time"""
        self._perform_action(lambda e, t: e.send_keys(t), locator_val, locator_type, text)

    def is_displayed(self, locator_val, locator_type="id"):
        """Check if element is displayed with optional wait time"""
        try:
            element = self._wait_for_element(locator_val, locator_type)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def is_enabled(self, locator_val, locator_type="id"):
        """Check if element is enabled with optional wait time"""
        try:
            element = self._wait_for_element(locator_val, locator_type)
            return element.is_enabled()
        except NoSuchElementException:
            return False

    def select_by_visible_text(self, locator_val, text, locator_type="id"):
        """Select an option by visible text in a dropdown"""
        self._perform_action(lambda e, t: Select(e).select_by_visible_text(t), locator_val, locator_type, text)

    def switch_to_window(self, window_number=0):
        """Switch to a new window or a tab"""
        windows = self.driver.window_handles
        if window_number < len(windows):
            self.driver.switch_to.window(windows[window_number])
        else:
            raise IndexError("Window index out of range")

    def switch_to_iframe(self, locator_val, locator_type="id"):
        """Switch to the iframe"""
        WebDriverWait(self.driver, 15).until(
            EC.frame_to_be_available_and_switch_to_it((getattr(By, locator_type.upper()), locator_val)))

    def accept_alert(self):
        """Accept an alert"""
        Alert(self.driver).accept()

    def dismiss_alert(self):
        """Dismiss an alert"""
        Alert(self.driver).dismiss()

    def switch_to_alert(self):
        """Switch to an alert"""
        return Alert(self.driver)

    def take_screenshot(self, text):
        """Take a screenshot and log it with Allure"""
        file_name = f"{text}_{time.strftime('%d_%m_%y_%H_%M_%S')}.png"
        screenshot_path = f"../screenshots/{file_name}"
        self.driver.save_screenshot(screenshot_path)
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)
