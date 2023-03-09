import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser


def test_search_article_browserstack():
    with allure.step("Tap wiki_search field"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step("Enter request"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys("BrowserStack")
    with allure.step("Check search results"):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


def test_search_article_star_wars():
    with allure.step("Tap wiki_search field"):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    with allure.step("Enter request"):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys("Star Wars")
    with allure.step("Check results"):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))