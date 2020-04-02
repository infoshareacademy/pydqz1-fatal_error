import time
from ..pages.locators import CommonSignInLocators as Locators

class SignUpPage:

    
    def __init__(self, driver):
        super(SignUpPage, self).__init__(driver)
    #
#     def __init__(self, driver):
#         self.driver = driver
#         self.element = "css selector for element"
#         self.texts = "css selecotr for group of elements text"
#         #następne css selektory
#
#     def action_on_page(self):
#         self.driver.find_element_by_css_selector(self.element).click()
#
#     # nastepne metody dostepne na tej stronie
#
#     # metody mogą także obejmować pobranie i zapisanie w liście danych dostepnych na stronie:
#
#     def text_on_page(self):
#         elements = self.driver.find_elements_by_css_selector(self.texts)
#
 #       return [elements[x].text for x in range(len(elements))]  # czy ktoś jeszcze pamięta list comprehension? ;)