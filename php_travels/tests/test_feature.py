import pytest
import time

@pytest.mark.usefixtures('setup_ch')
class TestTours:

    def test_all_fields(self, setup_ch):
        self.search_feature.search_tours(town='Egypt', date='27/02/2020', guests='2', trip='Private')
        time.sleep(0.5)
        #TESTY SPRAWDZAJĄCE CZY KATEGORIE SIĘ NIE ZMIENIŁY
        assert 'Nile Egypt, Egypt' in self.search_feature.tours_assert_cat_location()
        assert '27/02/2020' in self.search_feature.tours_assert_cat_date()
        assert '2' in self.search_feature.tours_assert_cat_guests()
        assert '                    Private                ' in self.search_feature.tours_assert_cat_type()
        # TESTY SPRAWDZAJĄCE WYNIK
        assert 1 == len(self.search_feature.assert_prices_list())
        assert '300' in self.search_feature.assert_prices_list()[0]
        assert 'Spectaculars Of The…' in self.search_feature.assert_names_list()
        assert 'Alexandria' in self.search_feature.assert_locations_list()

    # test gdy puste jest pole typu miasta
    def test_empty_city_field(self, setup_ch):
        self.search_feature.search_tours(date='27/02/2020', guests='2', trip='Private')
        time.sleep(1)
        assert 2 == len(self.search_feature.assert_prices_list())
        assert '300' in self.search_feature.assert_prices_list()[0]
        assert 'Spectaculars Of The…' in self.search_feature.assert_names_list()
        assert 'Alexandria' in self.search_feature.assert_locations_list()

    # test gdy puste jest pole daty
    def test_empty_date_field(self, setup_ch):
        self.search_feature.search_tours(town='Egypt', guests='2', trip='Private')
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # test gdy puste jest pole typu wycieczki
    def test_empty_tour_type_field(self, setup_ch):
        self.search_feature.search_tours(town='Egypt', date='27/02/2020', guests='2')
        time.sleep(3)
        assert 1 == len(self.search_feature.assert_prices_list())
        assert '300' in self.search_feature.assert_prices_list()[0]
        assert 'Spectaculars Of The…' in self.search_feature.assert_names_list()
        assert 'Alexandria' in self.search_feature.assert_locations_list()


    # test sprawdzający czy kategorię się zapamiętują
    @pytest.mark.skip('Bugged Guests field')
    def test_save_categories(self, setup_ch):
        self.search_feature.search_tours(town='Egypt', date='27/02/2020', guests='4', trip='Private')
        time.sleep(3)
        assert 'Nile Egypt, Egypt' in self.search_feature.tours_assert_cat_location()
        assert '27/02/2020' in self.search_feature.tours_assert_cat_date()
        assert '4' in self.search_feature.tours_assert_cat_guests()
        assert '                    Private                ' in self.search_feature.tours_assert_cat_type()


@pytest.mark.usefixtures('setup_ch')
class TestVisa:
    # testuje visa z wypelnionymi polami
    def test_filled_1st_2nd_country(self, setup_ch):
        self.search_feature.search_visa(first_country="Poland", second_country="Germany")
        time.sleep(5)
        list_of_assert_elements = self.search_feature.visa_result_text()
        assert list_of_assert_elements == ['Poland ➔ Germany']

    # testuje visa z pustym polem second country
    def test_empty_2nd_country(self, setup_ch):
        self.search_feature.search_visa(first_country="Poland")
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # testuje visa z pustym polem first country
    def test_empty_1st_country(self, setup_ch):
        self.search_feature.search_visa(second_country="Germany")
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # testuje visa z pustymi polami 1st i 2nd country
    def test_empty_1st_2nd_country(self, setup_ch):
        self.search_feature.search_visa()
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # Testuje visa z takimi samymi wybranymi państwami
    def test_same_1st_2nd_country(self, setup_ch):
        self.search_feature.search_visa(first_country="Poland", second_country="Poland")
        time.sleep(5)
        list_of_assert_elements = self.search_feature.visa_result_text()
        assert list_of_assert_elements == ['Poland ➔']

    # testuje visa randomowymi wartosciami z listy
    def test_random_way(self, setup_ch):
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



@pytest.mark.usefixtures('setup_ch')
class TestCars:
    # testuje cars z wypelnionymi polami
    def test_all_fields_filled(self, setup_ch):
        self.search_feature.search_cars(pick_up_town="Manchester", drop_off_town="Manchester", pick_up_date="27/06/2020", drop_off_date="28/06/2020")
        time.sleep(2)
        assert 1 == len(self.search_feature.assert_prices_list())
        assert '80' in self.search_feature.assert_prices_list()[0]
        assert 'Kia Pacanto 2014' in self.search_feature.assert_names_list()
        assert 'Manchester' in self.search_feature.assert_locations_list()

    # test z pustym pick up location
    def test_empty_pick_up_location(self, setup_ch):
        self.search_feature.search_cars(drop_off_town="Manchester", pick_up_date="27/06/2020", drop_off_date="28/06/2020")
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # test z pustym drop off location
    @pytest.mark.skip('Clearing drop off location is impossible')
    def test_empty_drop_off_location(self, setup_ch):
        self.search_feature.search_cars(pick_up_town="Manchester", pick_up_date="27/06/2020", drop_off_date="28/06/2020")
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # test z pustym pick up date
    def test_empty_pick_up_date(self, setup_ch):
        self.search_feature.search_cars(pick_up_town="Manchester", drop_off_town="Manchester", drop_off_date="28/06/2020")
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}

    # test z pustym drop off date
    def test_empty_drop_off_date(self, setup_ch):
        self.search_feature.search_cars(pick_up_town="Manchester", drop_off_town="Manchester", pick_up_date="27/06/2020")
        time.sleep(2)
        list_of_assert_elements = self.search_feature.get_search_bar_text_categories()
        assert set(list_of_assert_elements) <= {'hotels', 'flights', 'tours', 'ivisa', 'cars'}
