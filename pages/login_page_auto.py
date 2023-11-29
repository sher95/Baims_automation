from pages.base_page import BasePage
from utilities.config_reader import read_configuration


class Login(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login_popup(self):
        self.click_element(read_configuration("locators", "login_button_xpath"), "xpath")
        self.is_displayed(read_configuration("locators", "login_welcome_xpath"), "xpath"), "Login popup is not displayed"

    def click_sign_in_using_email(self):
        self.click_element(read_configuration("locators", "sign_in_using_email_xpath"), "xpath")

    def enter_email(self, email_text):
        self.send_text(email_text, read_configuration("locators", "email_field_name"), "name")

    def enter_password(self, password_text):
        self.send_text(password_text, read_configuration("locators", "password_field_name"), "name")

    def click_sign_in_button(self):
        self.click_element(read_configuration("locators", "sign_in_button_xpath"), "xpath")

    def check_signed_in_successful(self):
        self.is_displayed(read_configuration("locators", "signed_in_image_xpath"), "xpath"), "Image of account is not displayed"

    def invalid_credential_error_displayed(self):
        return self.get_element(read_configuration("locators", "invalid_cred_error_xpath"), "xpath")
