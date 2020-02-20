import pytest
import time


# # pojedyńczy test odnośnie danej funkcjonalności np. czy jak wpiszę w wyszukiwarkę tekst to mi wyskoczy dobry wynik?
#     def test_numerouno(self):
#         self.driver.get('http://www.kurs-selenium.pl/demo/') # -> otwieramy testową stronę
#         page_one = PageOne(self.driver) # -> stworzenie page objectu z przypisaniem mu webdrivera
#         page_one.action_on_page() # -> wywołanie zamierzonej akcji na stronie
#
# list_of_assert_elements = page_one.text_on_page() assert list_of_assert_elements == ['expected 1', 'expected 2'] #
# assercja na metodzie zwracająco liste elementów # np. listę samochodów ze strony z moją oczekiwaną listą samochodów


# klasa z testami dotyczącymi jednej funkcjonalności:



@pytest.mark.usefixtures('setup')
class TestTours:

    def test_tours(self, setup):
        self.search_feature.click_on_tours()
        time.sleep(5)


@pytest.mark.usefixtures('setup')
class TestVisa:
    # testuje visa happy pathem
    def test_visa_happy_path(self, setup):
        self.search_feature.click_on_visa()
        self.search_feature.visa_first_country_select('Poland')
        self.search_feature.visa_second_country_select('Germany')
        self.search_feature.visa_search_button_click()
        time.sleep(5)
        list_of_assert_elements = self.search_feature.visa_result_text()
        assert list_of_assert_elements == ['Poland ➔ Germany']

    # testuje visa randomowymi wartosciami z listy
    def test_visa_random_way(self, setup):
        self.search_feature.click_on_visa()
        first_country = self.search_feature.visa_choose_random_first_country()
        second_country = self.search_feature.visa_choose_random_second_country()
        self.search_feature.visa_search_button_click()
        time.sleep(5)
        list_of_assert_elements = self.search_feature.visa_result_text()
        if first_country != second_country:
            assert list_of_assert_elements == [first_country + ' ➔ ' + second_country]
        else:
            assert list_of_assert_elements == [first_country + ' ➔']


        # self.search_feature.visa_first_country_select('Poland')
        # self.search_feature.visa_second_country_select('Germany')
        # self.search_feature.visa_search_button_click()
        # time.sleep(5)
        # list_of_assert_elements = self.search_feature.visa_result_text()
        # assert list_of_assert_elements == ['Poland ➔ Germany']


    # def test_visa_empty_fields(self, setup):
    #     self.search_feature.click_on_visa()
    #     self.search_feature.visa_first_country_select('')
    #     self.search_feature.visa_second_country_select('')
    #     self.search_feature.visa_search_button_click()
    #     time.sleep(3)
    #     list_of_assert_elements = self.search_feature.visa_alert_text()
    #     assert 1 == 1

    # def test_visa_invalid_data(self, setup):
    #     self.search_feature.click_on_visa()
    #     self.driver.find_element_by_css_selector(self.search_feature.Visa_Select_Country_First).click()
    #     self.driver.find_element_by_css_selector(self.search_feature.Visa_Select_Country_First).send_keys('FDSAfdsa')
    #     list_of_assert_elements_first = self.search_feature.visa_stupid_data_no_found()
    #     self.search_feature.click_on_visa()
    #     list_of_assert_elements_first_country = self.search_feature.visa_first_country_check_text()
    #     time.sleep(4)
    #     self.driver.find_element_by_css_selector(self.Visa_Select_Country_Second).click()
    #     self.driver.find_element_by_css_selector(self.Visa_Select_Country_Second).send_keys('fdasfas')
    #     list_of_assert_elements_second = self.search_feature.visa_stupid_data_no_found()
    #     self.search_feature.click_on_visa()
    #     list_of_assert_elements_second_country = self.search_feature.visa_second_country_check_text()
    #     time.sleep(4)
    #     self.search_feature.visa_search_button_click()
    #     time.sleep(3)
    #     assert list_of_assert_elements_first == 'No matches found'
    #     assert list_of_assert_elements_second == 'No matches found'
    #     assert list_of_assert_elements_first_country == """
    #                     Select                        Country                    """
    #     assert list_of_assert_elements_second_country == """
    #                     Select                        Country                    """