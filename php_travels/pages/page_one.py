from selenium.webdriver.common.keys import Keys
from random import choice
import time


class SearchFeature:

    def __init__(self, driver):
        self.driver = driver
        self.tours_search_by = '#s2id_autogen10 a'
        self.tours_date = '#tchkin input'
        self.tours_guests = '#adults'
        self.tours_select_type = '#s2id_tourtype a'
        self.tours_search_button = '#tours button'

        self.tours_assert_category_location = '#s2id_autogen2 span'
        self.tours_assert_category_date = '#tchkin input'
        self.tours_assert_category_guests = "#adults [selected]"
        self.tours_assert_category_tours_type = '#tourtype [selected]'
        self.tours_assert_result_prices_list = ".fs26 b"
        self.tours_assert_result_tours_names_list = ".row .RTL b"
        self.tours_assert_result_tours_locations_list = ".row .ellipsisFIX"
        self.tours_assert_calendar_view = '[class*="dropdown-menu"][style*="display: block;"]'



        self.Main_Button_Hotels = '#body-section li:nth-child(1) > a'
        self.Main_Button_Flights = '#body-section li:nth-child(2) > a'
        self.Main_Button_Tours = '#body-section li:nth-child(3) > a'
        self.Main_Button_Cars = '#body-section li:nth-child(4) > a'
        self.Main_Button_Visa = '#body-section li:nth-child(5) > a'
        self.Cars_Location_Pick = '#s2id_carlocations .select2-chosen'
        self.Cars_Location_Drop = '#s2id_carlocations2 .select2-chosen'
        self.Cars_Date_Pick = '#departcar.form.input-lg.RTL'
        self.Cars_Time_Pick = '#cars :nth-child(4) select'
        self.Cars_Date_Drop = '#returncar.form.input-lg.RTL'
        self.Cars_Time_Drop = '#cars :nth-child(6) select'
        self.Cars_Search_Button = '#cars button'
        self.Visa_Select_Country_First = '#s2id_autogen4 > a'
        self.Visa_Select_Country_Second = '#s2id_autogen6 > a'
        self.Visa_Search_Button = '#ivisa button'
        self.Visa_assert_result_text = '#body-section h3'
        self.Visa_assert_search_bar_categories = '#body-section li'
        self.Visa_first_country_check_text = '#s2id_autogen4 > a >span:nth-child(1)'
        self.Visa_second_country_check_text = '#s2id_autogen6 > a >span:nth-child(1)'
        self.Visa_no_results_found = '#select2-drop > ul > li'
        self.Visa_country_list = '#select2-drop li > div'
        # następne css selektory

    # przerobić to na go_to, żeby przechodziło na odpowiedni bar

    def click_on_tours(self):
        self.driver.find_element_by_css_selector(self.Main_Button_Tours).click()

    def tours_search_city(self, town='Egypt'):
        self.driver.find_element_by_css_selector(self.tours_search_by).click()
        self.driver.find_element_by_css_selector(self.tours_search_by).send_keys(town)
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(self.tours_search_by).send_keys(Keys.ENTER)

    def tours_change_date(self, date='27/02/2020'):
        self.driver.find_element_by_css_selector(self.tours_date).click()
        self.driver.find_element_by_css_selector(self.tours_date).clear()
        self.driver.find_element_by_css_selector(self.tours_date).send_keys(date)

    def tours_guests_number(self, guests):
        self.driver.find_element_by_css_selector(self.tours_guests).click()
        time.sleep(0.5)
        self.driver.find_element_by_css_selector("#adults [value='" + guests + "']").click()

    def tours_trip_type(self, trip):
        self.driver.find_element_by_css_selector(self.tours_select_type).click()
        self.driver.find_element_by_css_selector(self.tours_select_type).send_keys(trip)
        self.driver.find_element_by_css_selector(self.tours_select_type).send_keys(Keys.ENTER)

    def tours_search_button_click(self):
        self.driver.find_element_by_css_selector(self.tours_search_button).click()

    def tours_assert_cat_location(self):
        elements = self.driver.find_elements_by_css_selector(self.tours_assert_category_location)
        return [elements[x].text for x in range(len(elements))]

    def tours_assert_cat_date(self):
        element = self.driver.find_element_by_css_selector(self.tours_assert_category_date).get_attribute("value")
        return element

    def tours_assert_cat_guests(self):
        element = self.driver.find_element_by_css_selector(self.tours_assert_category_guests).get_attribute("value")
        return element

    def tours_assert_cat_type(self):
        elements = self.driver.find_elements_by_css_selector(self.tours_assert_category_tours_type)
        return [elements[x].text for x in range(len(elements))]

    def tours_assert_prices_list(self):
        elements = self.driver.find_elements_by_css_selector(self.tours_assert_result_prices_list)
        return [elements[x].text for x in range(len(elements))]

    def tours_assert_names_list(self):
        elements = self.driver.find_elements_by_css_selector(self.tours_assert_result_tours_names_list)
        return [elements[x].text for x in range(len(elements))]

    def tours_assert_locations_list(self):
        elements = self.driver.find_elements_by_css_selector(self.tours_assert_result_tours_locations_list)
        return [elements[x].get_attribute('title') for x in range(len(elements))]






    def click_on_visa(self):
        self.driver.find_element_by_css_selector(self.Main_Button_Visa).click()

    def visa_first_country_select(self, first_country):
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_First).click()
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_First).send_keys(first_country)
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_First).send_keys(Keys.ENTER)

    def visa_second_country_select(self, second_country):
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_Second).click()
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_Second).send_keys(second_country)
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_Second).send_keys(Keys.ENTER)

    def visa_search_button_click(self):
        self.driver.find_element_by_css_selector(self.Visa_Search_Button).click()

    def visa_choose_random_first_country(self):
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_First).click()
        elements = self.driver.find_elements_by_css_selector(self.Visa_country_list)
        country_list = [elements[x].text for x in range(len(elements))]
        country_list.remove('Select Country')
        first_country = choice(country_list)
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_First).send_keys(first_country)
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_First).send_keys(Keys.ENTER)
        time.sleep(1)
        return first_country

    def visa_choose_random_second_country(self):
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_Second).click()
        elements = self.driver.find_elements_by_css_selector(self.Visa_country_list)
        country_list = [elements[x].text for x in range(len(elements))]
        country_list.remove('Select Country')
        second_country = choice(country_list)
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_Second).send_keys(second_country)
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(self.Visa_Select_Country_Second).send_keys(Keys.ENTER)
        time.sleep(1)
        return second_country

    def visa_result_text(self):
        elements = self.driver.find_elements_by_css_selector(self.Visa_assert_result_text)
        return [elements[x].text for x in range(len(elements))]

    def get_search_bar_text_categories(self):
        elements = self.driver.find_elements_by_css_selector(self.Visa_assert_search_bar_categories)
        return [elements[x].get_attribute('data-title') for x in range(len(elements))]