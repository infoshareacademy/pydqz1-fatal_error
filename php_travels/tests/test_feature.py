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

    def test_visa_happy_path(self, setup):
        self.search_feature.click_on_visa()
        self.search_feature.visa_first_country_select('Poland')
        self.search_feature.visa_second_country_select('Germany')
        self.search_feature.visa_search_button_click()
        time.sleep(3)
        list_of_assert_elements = self.search_feature.visa_result_text()
        assert list_of_assert_elements == ['Poland ➔ Germany']

