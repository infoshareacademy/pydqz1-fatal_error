import pytest
import time







@pytest.mark.usefixtures('setup')
class TestTours:

# [x] assercja kategorii - czy nasze wybrane się nie zmieniły i zachowały
# [tak jakby x] assercja od kwoty zależnej od osób (150$ za osoby czyli przy 2 osobach to 300$)
# [x] assercja od tego czy nazwa danej wycieczki jest taka jak trzeba ('Spectaculars Of The…')
# [x] assercja od tego czy nazwa danej wycieczki jest taka jak trzeba ('Alexandria')
# [] assercja tego czy jest widoczny/klikalny przycisk "Details"
# [] napisać kod do tours dla randomowych wartości
    def test_all_fields_filled(self, setup):
        self.search_feature.click_on_tours()
        self.search_feature.tours_search_city('Egypt')
        self.search_feature.tours_change_date('27/02/2020')
        self.search_feature.tours_guests_number('2')
        self.search_feature.tours_trip_type('Private')
        self.search_feature.tours_search_button_click()
        time.sleep(3)
        #TESTY SPRAWDZAJĄCE CZY KATEGORIE SIĘ NIE ZMIENIŁY
        assert 'Nile Egypt, Egypt' in self.search_feature.tours_assert_cat_location()
        assert '27/02/2020' in self.search_feature.tours_assert_cat_date()
        assert '2' in self.search_feature.tours_assert_cat_guests()
        assert '                    Private                ' in self.search_feature.tours_assert_cat_type()
        # TESTY SPRAWDZAJĄCE WYNIK
        assert 1 == len(self.search_feature.tours_assert_prices_list())
        assert '300' in self.search_feature.tours_assert_prices_list()[0]
        assert 'Spectaculars Of The…' in self.search_feature.tours_assert_names_list()
        assert 'Alexandria' in self.search_feature.tours_assert_locations_list()

    def test_empty_city_field(self, setup):
        self.search_feature.click_on_tours()
        self.search_feature.tours_change_date('27/02/2020')
        self.search_feature.tours_guests_number('2')
        self.search_feature.tours_trip_type('Private')
        self.search_feature.tours_search_button_click()
        time.sleep(3)
        assert 2 == len(self.search_feature.tours_assert_prices_list())
        assert '300' in self.search_feature.tours_assert_prices_list()[0]
        assert 'Spectaculars Of The…' in self.search_feature.tours_assert_names_list()
        assert 'Alexandria' in self.search_feature.tours_assert_locations_list()

    # test gdy puste jest pole daty
    def test_empty_date_field(self, setup):
        self.search_feature.click_on_tours()
        self.search_feature.tours_search_city('Egypt')
        self.search_feature.tours_change_date('')
        self.search_feature.tours_guests_number('2')
        self.search_feature.tours_trip_type('Private')
        self.search_feature.tours_search_button_click()
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # test gdy puste jest pole typu wycieczki
    def test_empty_tour_type_field(self, setup):
        self.search_feature.click_on_tours()
        self.search_feature.tours_search_city('Egypt')
        self.search_feature.tours_change_date('27/02/2020')
        self.search_feature.tours_guests_number('2')
        self.search_feature.tours_search_button_click()
        time.sleep(3)
        assert 1 == len(self.search_feature.tours_assert_prices_list())
        assert '300' in self.search_feature.tours_assert_prices_list()[0]
        assert 'Spectaculars Of The…' in self.search_feature.tours_assert_names_list()
        assert 'Alexandria' in self.search_feature.tours_assert_locations_list()


    # test sprawdzający czy kategorię się zapamiętują
    @pytest.mark.skip('Bugged Guests field')
    def test_save_categories(self):
        self.search_feature.click_on_tours()
        self.search_feature.tours_search_city('Egypt')
        self.search_feature.tours_change_date('27/02/2020')
        self.search_feature.tours_guests_number('4')
        self.search_feature.tours_trip_type('Private')
        self.search_feature.tours_search_button_click()
        time.sleep(3)
        assert 'Nile Egypt, Egypt' in self.search_feature.tours_assert_cat_location()
        assert '27/02/2020' in self.search_feature.tours_assert_cat_date()
        assert '4' in self.search_feature.tours_assert_cat_guests()
        assert '                    Private                ' in self.search_feature.tours_assert_cat_type()


@pytest.mark.usefixtures('setup')
class TestVisa:
    # testuje visa z wypelnionymi polami
    def test_filled_1st_2nd_country(self, setup):
        self.search_feature.click_on_visa()
        self.search_feature.visa_first_country_select('Poland')
        self.search_feature.visa_second_country_select('Germany')
        self.search_feature.visa_search_button_click()
        time.sleep(5)
        list_of_assert_elements = self.search_feature.visa_result_text()
        assert list_of_assert_elements == ['Poland ➔ Germany']

    # testuje visa z pustym polem second country
    def test_empty_2nd_country(self, setup):
        self.search_feature.click_on_visa()
        self.search_feature.visa_first_country_select('Poland')
        self.search_feature.visa_search_button_click()
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # testuje visa z pustym polem first country
    def test_empty_1st_country(self, setup):
        self.search_feature.click_on_visa()
        self.search_feature.visa_second_country_select('Germany')
        self.search_feature.visa_search_button_click()
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # testuje visa z pustymi polami 1st i 2nd country
    def test_empty_1st_2nd_country(self, setup):
        self.search_feature.click_on_visa()
        self.search_feature.visa_search_button_click()
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # Testuje visa z takimi samymi wybranymi państwami
    def test_same_1st_2nd_country(self, setup):
        self.search_feature.click_on_visa()
        self.search_feature.visa_first_country_select('Poland')
        self.search_feature.visa_second_country_select('Poland')
        self.search_feature.visa_search_button_click()
        time.sleep(5)
        list_of_assert_elements = self.search_feature.visa_result_text()
        assert list_of_assert_elements == ['Poland ➔']

    # testuje visa randomowymi wartosciami z listy
    def test_random_way(self, setup):
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
