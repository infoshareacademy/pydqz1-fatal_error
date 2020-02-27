import pytest
from php_travels.pages.login_page import Login


@pytest.mark.usefixtures('setup_ch')
class TestPageFeature:

    def test_happy_path_login(self):  # -> testujemy proces logowania z poprawnymi danymi + zapamiętanie danych
        login_page = Login(self.driver)
        login_page.login_happy_path()

        list_of_assert_elements = login_page.left_menu_text()
        assert list_of_assert_elements == ["Bookings", "My Profile", "Wishlist", "Newsletter"]

    def test_forget_password_function(self):  # -> testujemy funkcje przywracania zapomnianego hasła
        login_page = Login(self.driver)
        login_page.login_forget_password()
        assert 'New Password sent to s.r@wp.pl, Kindly check email' in self.login_page.reset_password_text()

    def test_forget_password_function_with_wrong_mail(self):  # -> testujemy funkcje przywracania zapomnianego hasła, podając błedny email
        login_page = Login(self.driver)
        login_page.login_reset_password_wrong_mail()
        assert 'Email Not Found' in self.login_page.reset_password_wrong_mail_text()

    def test_empty_email_input(self):  # -> testujemy funkcje logowania bez podanego emaila
        login_page = Login(self.driver)
        login_page.login_empty_email()
        assert 'Invalid Email or Password' in self.login_page.empty_email_text()

    def test_empty_password_input(self):  # -> testujemy funkcje logowania bez podanego hasła
        login_page = Login(self.driver)
        login_page.login_empty_password()
        assert 'Invalid Email or Password' in self.login_page.empty_password_text()

    def test_logout(self):  # -> testujemy funcje wylogowania
        login_page = Login(self.driver)
        login_page.logout()
        assert 'LOGIN' in self.login_page.logout_text()

    def test_wrong_email_input(self):  # -> testujemy funkcje logowania z błednym adresem email
        login_page = Login(self.driver)
        login_page.login_wrong_email()
        assert 'Invalid Email or Password' in self.login_page.wrong_email_text()
