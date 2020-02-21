import pytest
from pages.page_one import PageOne



# klasa z testami dotyczącymi jednej funkcjonalności:
@pytest.mark.usefixtures('setup')
class TestPageFeature:

# pojedyńczy test odnośnie danej funkcjonalności np. czy jak wpiszę w wyszukiwarkę tekst to mi wyskoczy dobry wynik?
    def test_numerouno(self):
        page_one = PageOne(self.driver)  # -> stworzenie page objectu z przypisaniem mu webdrivera
        page_one.action_on_page()  # -> wywołanie zamierzonej akcji na stronie

        list_of_assert_elements = page_one.text_on_page()
        assert list_of_assert_elements == ['Sign Up']  # assercja na metodzie zwracająco liste elementów
        # np. listę samochodów ze strony z moją oczekiwaną listą samochodów



