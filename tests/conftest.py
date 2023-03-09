import pytest
from appium.options.android import UiAutomator2Options
from selene.support.shared import browser
from appium import webdriver
from utils import attach


@pytest.fixture(scope="function", autouse=True)
def driver_config():
    options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
            "bstack:options": {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": "sukhorukovam@gmail.com",
                "accessKey": "gWFspRczPJyxvV3Gsy1M",
            },
        }
    )

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield

    attach.add_video(browser)
    browser.quit()