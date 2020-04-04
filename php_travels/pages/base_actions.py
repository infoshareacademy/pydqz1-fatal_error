class BaseActions:


    def __init__(self, driver):
        self.driver = driver

    def click_on(self, css_selector):
        self.driver.find_element_by_css_selector(css_selector).click()

    def field_send_keys(self, css_selector, text):
        self.driver.find_element_by_css_selector(css_selector).send_keys(text)

    def assert_text_elements(self, css_selector):
        elements = self.driver.find_elements_by_css_selector(css_selector)
        return [elements[x].text for x in range(len(elements))]
