import pytest
from assertpy import assert_that
from pages.home_page import HomePage


# klasa z testami dotyczącymi jednej funkcjonalności:
@pytest.mark.usefixtures('setup')
class TestPageFeature:

# pojedyńczy test odnośnie danej funkcjonalności np. czy jak wpiszę w wyszukiwarkę tekst to mi wyskoczy dobry wynik?
    def test_numerouno(self):
        home_page = HomePage(self.driver)  # -> stworzenie page objectu z przypisaniem mu webdrivera
        home_page.action_on_page()  # -> wywołanie zamierzonej akcji na stronie

        list_of_assert_elements = home_page.text_left_menu()
        assert_that(list_of_assert_elements).is_equal_to(["My Profile"])   # assercja na metodzie zwracająco liste elementów
        # np. listę samochodów ze strony z moją oczekiwaną listą samochodów



