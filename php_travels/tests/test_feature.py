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
from selenium.webdriver.support import wait


@pytest.mark.usefixtures('setup')
class TestTours:

# assercja kategorii - czy nasze wybrane się nie zmieniły i zachowały
# assercja od kwoty zależnej od osób (150$ za osoby czyli przy 2 osobach to 300$)
# assercja od tego czy nazwa danej wycieczki jest taka jak trzeba ('Spectaculars Of The…')
# assercja od tego czy nazwa danej wycieczki jest taka jak trzeba ('Alexandria')
# assercja tego czy jest widoczny/klikalny przycisk "Details"

    def test_tours_happy_path(self, setup):
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

    def test_visa_empty_values(self, setup):
        self.search_feature.click_on_visa()
        self.search_feature.visa_search_button_click()
        time.sleep(2)
        assert 'VISA' in self.search_feature.get_nav_bar_content()

