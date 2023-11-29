import allure
import pytest
from pages.login_page_auto import Login
from pages.course_player_page import CoursePlayer
"""
1. I divided to classes, to use later and add related test cases
2. Before run course make sure course not opened before, otherwise join and start pages not appear
3. Each test method is configured to open a new Chrome browser instance.
Browser setup is isolated for each individual test method, providing a clean and independent testing environment.
This helps in preventing potential interference between test methods and ensures reliable and reproducible test executions.
"""


@pytest.mark.usefixtures("setup_teardown", "log_on_failure")
class TestSignIn:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_signin_using_email_invalid_credential(self):
        login_page = Login(self.driver)
        login_page.login_popup()
        login_page.click_sign_in_using_email()
        login_page.enter_email("Abdelrahman4040@gmail.com")
        login_page.enter_password("12345678")
        login_page.click_sign_in_button()

        actual_error_text = login_page.invalid_credential_error_displayed().text
        expected_error_text = "You seem to have a wrong email or password."
        assert actual_error_text == expected_error_text, f"Expected error: '{expected_error_text}', but found: '{actual_error_text}'"


@pytest.mark.usefixtures("setup_teardown", "log_on_failure")
class TestCoursePlayer:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_course_video_player_displayed(self):
        login_page = Login(self.driver)
        login_page.login_popup()
        login_page.click_sign_in_using_email()
        login_page.enter_email("Abdelrahman4040@gmail.com")
        login_page.enter_password("Or7m?x?@$rw?")
        login_page.click_sign_in_button()
        login_page.check_signed_in_successful()

        course_player = CoursePlayer(self.driver)
        course_player.navigate_to_url("https://app.baims.com/subjects/0299df5e85291809e14ee799b63622")
        course_player.click_join()
        course_player.click_start_watching()
        course_player.select_unit_of_courses("Unit 1 Big changes")
        course_player.validate_video_player_displayed()
