from selenium.webdriver.common.keys import Keys
from random import choice
import time
from pages.base_actions import BaseActions


class SearchFeature:

    def __init__(self, driver):
        self.driver = driver
        self.base_actions = BaseActions(driver)
        self.tours_search_by = '#s2id_autogen10 a'
        self.tours_date = '#tchkin input'
        self.tours_guests = '#adults'
        self.tours_select_type = '#s2id_tourtype a'
        self.tours_search_button = '#tours button'

        self.tours_assert_category_location = '#s2id_autogen2 span'
        self.tours_assert_category_date = '#tchkin input'
        self.tours_assert_category_guests = "#adults [selected]"
        self.tours_assert_category_tours_type = '#tourtype [selected]'
        self.assert_result_prices_list = ".fs26 b"
        self.assert_result_names_list = ".row .RTL b"
        self.assert_result_tours_locations_list = ".row .ellipsisFIX"
        self.tours_assert_calendar_view = '[class*="dropdown-menu"][style*="display: block;"]'

        self.Main_Button_Hotels = '#body-section li:nth-child(1) > a'
        self.Main_Button_Flights = '#body-section li:nth-child(2) > a'
        self.Main_Button_Tours = '#body-section li:nth-child(3) > a'
        self.Main_Button_Cars = '#body-section li:nth-child(4) > a'
        self.Main_Button_Visa = '#body-section li:nth-child(5) > a'

        self.Cars_Location_Pick = '#s2id_carlocations a'
        self.Cars_Location_Drop = '#s2id_carlocations2 a'
        self.Cars_Date_Pick = '#departcar.form.input-lg.RTL'
        self.Cars_Time_Pick = '#cars :nth-child(4) select'
        self.Cars_Date_Drop = '#returncar.form.input-lg.RTL'
        self.Cars_Time_Drop = '#cars :nth-child(6) select'
        self.Cars_Search_Button = '#cars button'

        self.Visa_Select_Country_First = '#s2id_autogen4 > a'
        self.Visa_Select_Country_Second = '#s2id_autogen6 > a'
        self.Visa_Search_Button = '#ivisa button'
        self.Visa_assert_result_text = '#body-section h3'
        self.assert_search_bar_categories = '#body-section li'
        self.Visa_first_country_check_text = '#s2id_autogen4 > a >span:nth-child(1)'
        self.Visa_second_country_check_text = '#s2id_autogen6 > a >span:nth-child(1)'
        self.Visa_no_results_found = '#select2-drop > ul > li'
        self.Visa_country_list = '#select2-drop li > div'

    def tours_assert_cat_location(self):
        return self.base_actions.assert_text_elements(self.tours_assert_category_location)

    def tours_assert_cat_date(self):
        return self.base_actions.assert_attribute_element(self.tours_assert_category_date, "value")

    def tours_assert_cat_guests(self):
        return self.base_actions.assert_attribute_element(self.tours_assert_category_guests, "value")

    def tours_assert_cat_type(self):
        return self.base_actions.assert_text_elements(self.tours_assert_category_tours_type)

    def assert_prices_list(self):
        return self.base_actions.assert_text_elements(self.assert_result_prices_list)

    def assert_names_list(self):
        return self.base_actions.assert_text_elements(self.assert_result_names_list)

    def assert_locations_list(self):
        return self.base_actions.assert_attribute_element(self.assert_result_tours_locations_list, 'title')

    def click_on_visa(self):
        self.base_actions.click_on(self.Main_Button_Visa)

    def visa_first_country_select(self, first_country):
        self.base_actions.click_on(self.Visa_Select_Country_First)
        self.base_actions.field_send_keys(self.Visa_Select_Country_First, first_country)
        self.base_actions.field_send_keys_enter(self.Visa_Select_Country_First)

    def visa_second_country_select(self, second_country):
        self.base_actions.click_on(self.Visa_Select_Country_Second)
        self.base_actions.field_send_keys(self.Visa_Select_Country_Second, second_country)
        self.base_actions.field_send_keys_enter(self.Visa_Select_Country_Second)

    def visa_search_button_click(self):
        self.base_actions.click_on(self.Visa_Search_Button)

    def visa_choose_random_first_country(self):
        self.base_actions.click_on(self.Visa_Select_Country_First)
        country_list = self.base_actions.assert_text_elements(self.Visa_country_list)
        country_list.remove('Select Country')
        first_country = choice(country_list)
        self.base_actions.field_send_keys(self.Visa_Select_Country_First, first_country)
        time.sleep(0.5)
        self.base_actions.field_send_keys_enter(self.Visa_Select_Country_First)
        time.sleep(1)
        return first_country

    def visa_choose_random_second_country(self):
        self.base_actions.click_on(self.Visa_Select_Country_Second)
        country_list = self.base_actions.assert_text_elements(self.Visa_country_list)
        country_list.remove('Select Country')
        second_country = choice(country_list)
        self.base_actions.field_send_keys(self.Visa_Select_Country_Second, second_country)
        time.sleep(0.5)
        self.base_actions.field_send_keys_enter(self.Visa_Select_Country_Second)
        time.sleep(1)
        return second_country

    def visa_result_text(self):
        return self.base_actions.assert_text_elements(self.Visa_assert_result_text)

    def get_search_bar_text_categories(self):
        return self.base_actions.base_get_search_bar_text_categories()

    def search_tours(self, town="", date="", guests="", trip=""):
        self.base_actions.click_on(self.Main_Button_Tours)
        if town != "":
            self.base_actions.click_on(self.tours_search_by)
            self.base_actions.field_send_keys(self.tours_search_by, town)
            time.sleep(0.5)
            self.base_actions.field_send_keys_enter(self.tours_search_by)
        if date != "":
            self.base_actions.click_on(self.tours_date)
            self.base_actions.field_clear(self.tours_date)
            self.base_actions.field_send_keys(self.tours_date, date)
        if guests != "":
            self.base_actions.click_on(self.tours_guests)
            time.sleep(0.5)
            self.base_actions.click_on("#adults [value='" + guests + "']")
        if trip != "":
            self.base_actions.click_on(self.tours_select_type)
            self.base_actions.field_send_keys(self.tours_select_type, trip)
            self.base_actions.field_send_keys_enter(self.tours_select_type)
        self.base_actions.click_on(self.tours_search_button)

    def search_cars(self, pick_up_town="", drop_off_town="", pick_up_date="", drop_off_date=""):
        self.base_actions.click_on(self.Main_Button_Cars)
        if pick_up_town != "":
            self.base_actions.click_on(self.Cars_Location_Pick)
            self.base_actions.field_send_keys(self.Cars_Location_Pick, pick_up_town)
            time.sleep(0.5)
            self.base_actions.field_send_keys_enter(self.Cars_Location_Pick)
        if drop_off_town != "":
            self.base_actions.click_on(self.Cars_Location_Drop)
            self.base_actions.field_send_keys(self.Cars_Location_Drop, drop_off_town)
            time.sleep(0.5)
            self.base_actions.field_send_keys_enter(self.Cars_Location_Drop)
        if pick_up_date != "":
            self.base_actions.click_on(self.Cars_Date_Pick)
            self.base_actions.field_clear(self.Cars_Date_Pick)
            self.base_actions.field_send_keys(self.Cars_Date_Pick, pick_up_date)
        if drop_off_date != "":
            self.base_actions.click_on(self.Cars_Date_Drop)
            self.base_actions.field_clear(self.Cars_Date_Drop)
            self.base_actions.field_send_keys(self.Cars_Date_Drop, drop_off_date)
        self.base_actions.click_on(self.Cars_Search_Button)

    def search_visa(self, first_country="", second_country=""):
        self.base_actions.click_on(self.Main_Button_Visa)
        if first_country != "":
            self.base_actions.click_on(self.Visa_Select_Country_First)
            self.base_actions.field_send_keys(self.Visa_Select_Country_First, first_country)
            self.base_actions.field_send_keys_enter(self.Visa_Select_Country_First)
        if second_country != "":
            self.base_actions.click_on(self.Visa_Select_Country_Second)
            self.base_actions.field_send_keys(self.Visa_Select_Country_Second, second_country)
            self.base_actions.field_send_keys_enter(self.Visa_Select_Country_Second)
        self.base_actions.click_on(self.Visa_Search_Button)
