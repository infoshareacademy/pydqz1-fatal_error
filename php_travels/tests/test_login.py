import pytest
from php_travels.pages.login_page import Login


@pytest.mark.usefixtures('setup_ch')
class TestPageFeature:

    def test_login_happy_path(self):  # -> testujemy proces logowania z poprawnymi danymi + zapamiętanie danych
        page_one = Login(self.driver)
        page_one.login_happy_path()

        list_of_assert_elements = page_one.left_menu_text()
        assert list_of_assert_elements == ["Bookings", "My Profile", "Wishlist", "Newsletter"]

    def test_forget_password(self):  # -> testujemy funkcje przywracania zapomnianego hasła
        page_one = Login(self.driver)
        page_one.login_forget_password()

        list_of_assert_elements = page_one.reset_password_text()
        assert list_of_assert_elements == ["New Password sent to s.r@wp.pl, Kindly check email"]

    def test_empty_email(self):  # -> testujemy funkcje logowania bez podanego emaila
        page_one = Login(self.driver)
        page_one.login_empty_email()

        list_of_assert_elements = page_one.empty_email_text()
        assert list_of_assert_elements == ["Invalid Email or Password"]

    def test_empty_password(self):  # -> testujemy funkcje logowania bez podanego hasła
        page_one = Login(self.driver)
        page_one.login_empty_password()

        list_of_assert_elements = page_one.empty_password_text()
        assert list_of_assert_elements == ["Invalid Email or Password"]

    def test_logout(self):  # -> testujemy funcje wylogowania
        page_one = Login(self.driver)
        page_one.logout()

        list_of_assert_elements = page_one.logout_text()
        assert list_of_assert_elements == ["LOGIN"]

    def test_wrong_email(self):  # -> testujemy funkcje logowania z błednym adresem email
        page_one = Login(self.driver)
        page_one.login_wrong_email()

        list_of_assert_elements = page_one.wrong_email_text()
        assert list_of_assert_elements == ["Invalid Email or Password"]
