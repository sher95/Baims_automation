import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utilities.config_reader import read_configuration
import allure
from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, setup_teardown):
    yield
    item = request.node
    driver = setup_teardown
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name=f"Fail{request.function.__name__}_{time.strftime('%y_%m_%d_%H_%M')}", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome"], scope="function")
def setup_teardown(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(read_configuration("basic info", "site_url"))
    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.quit()
