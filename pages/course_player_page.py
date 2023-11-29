from pages.base_page import BasePage
from utilities.config_reader import read_configuration


class CoursePlayer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_join(self):
        self.click_element(read_configuration("locators", "join_button_xpath"), "xpath")

    def click_start_watching(self):
        self.click_element(read_configuration("locators", "start_watching_button_xpath"), "xpath")

    def select_unit_of_courses(self, text):
        self.click_element_by_text(text=text)

    def validate_video_player_displayed(self):
        self.switch_to_iframe(read_configuration("locators", "video_iframe_xpath"), "xpath")
        self.is_displayed(read_configuration("locators", "video_player_xpath"), "xpath"), "Video player is not displayed"
