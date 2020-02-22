import pytest
from php_travels.pages.login_page import Login


@pytest.mark.usefixtures('setup_ch')
class TestPageFeature:

    def test_login_happy_path(self):  # -> testujemy proces logowania z poprawnymi danymi + zapamiętanie danych
        login_page = Login(self.driver)
        login_page.login_happy_path()

        list_of_assert_elements = login_page.left_menu_text()
        assert list_of_assert_elements == ["Bookings", "My Profile", "Wishlist", "Newsletter"]

    def test_forget_password(self):  # -> testujemy funkcje przywracania zapomnianego hasła
        login_page = Login(self.driver)
        login_page.login_forget_password()

        list_of_assert_elements = login_page.reset_password_text()
        assert list_of_assert_elements == ["New Password sent to s.r@wp.pl, Kindly check email"]

    def test_empty_email(self):  # -> testujemy funkcje logowania bez podanego emaila
        login_page = Login(self.driver)
        login_page.login_empty_email()

        list_of_assert_elements = login_page.empty_email_text()
        assert list_of_assert_elements == ["Invalid Email or Password"]

    def test_empty_password(self):  # -> testujemy funkcje logowania bez podanego hasła
        login_page = Login(self.driver)
        login_page.login_empty_password()

        list_of_assert_elements = login_page.empty_password_text()
        assert list_of_assert_elements == ["Invalid Email or Password"]

    def test_logout(self):  # -> testujemy funcje wylogowania
        login_page = Login(self.driver)
        login_page.logout()

        list_of_assert_elements = login_page.logout_text()
        assert list_of_assert_elements == ["LOGIN"]

    def test_wrong_email(self):  # -> testujemy funkcje logowania z błednym adresem email
        login_page = Login(self.driver)
        login_page.login_wrong_email()

        list_of_assert_elements = login_page.wrong_email_text()
        assert list_of_assert_elements == ["Invalid Email or Password"]
