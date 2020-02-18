from selenium.webdriver.common.keys import Keys


class SearchFeature:

    def __init__(self, driver):
        self.driver = driver
        self.tours_search_by = '#select2-drop input'
        self.tours_date = '#tchkin input'
        self.tours_guests = '#adults'
        self.tours_select_type = '#select2-drop > div > input'
        self.tours_search_button = '#tours button'
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
        self.Visa_assert_text = "#body-section h3"
        # następne css selektory

    # przerobić to na go_to, żeby przechodziło na odpowiedni bar

    def click_on_tours(self):
        self.driver.find_element_by_css_selector(self.Main_Button_Tours).click()

    # def tours_search_city(self):
    #     self.driver.find_element_by_css_selector(self.tours_search_by).clear()
    #     self.driver.find_element_by_css_selector(self.tours_search_by).send_keys('Egypt')
    #     self.driver.find_element_by_css_selector(self.tours_search_by).send_keys(Keys.ENTER)
    #
    # def tours_change_date(self):
    #     self.driver.find_element_by_css_selector(self.tours_date).clear()
    #     self.driver.find_element_by_css_selector(self.tours_date).send_keys('20/02/2020')
    #     self.driver.find_element_by_css_selector(self.tours_date).send_keys(Keys.ENTER)
    #
    # def tours_guests_number(self):
    #     self.driver.find_element_by_css_selector(self.tours_guests).click()
    #     self.driver.find_element_by_css_selector('# adults > option:nth-child(5)').click()
    #
    #
    # def tours_trip_type(self):
    #     self.driver.find_element_by_css_selector(self.tours_select_type).click()

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

    def visa_result_text(self):
        elements = self.driver.find_elements_by_css_selector(self.Visa_assert_text)
        return [elements[x].text for x in range(len(elements))]
