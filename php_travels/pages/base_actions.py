from selenium.webdriver.common.keys import Keys


class BaseActions:
    def __init__(self, driver):
        self.driver = driver

    def field_send_keys(self, css_selector, text):
        self.driver.find_element_by_css_selector(css_selector).send_keys(text)

    def field_send_keys_enter(self, css_selector):
        self.driver.find_element_by_css_selector(css_selector).send_keys(Keys.ENTER)

    def click_on(self, css_selector):
        self.driver.find_element_by_css_selector(css_selector).click()

    def assert_text_elements(self, css_selector):
        elements = self.driver.find_elements_by_css_selector(css_selector)
        return [elements[x].text for x in range(len(elements))]

    def assert_attribute_element(self, css_selector, attribute):
        element = self.driver.find_element_by_css_selector(css_selector).get_attribute(attribute)
        return element

    def field_clear(self, css_selector):
        self.driver.find_element_by_css_selector(css_selector).clear()

    def base_get_search_bar_text_categories(self):
        elements = self.driver.find_elements_by_css_selector('#body-section li')
        return [elements[x].get_attribute('data-title') for x in range(len(elements))]
