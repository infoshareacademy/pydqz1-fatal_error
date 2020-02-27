import pytest
from php_travels.pages.login_page import Login


@pytest.mark.usefixtures('setup_ch')
class TestPageFeature:

    # testujemy proces logowania z poprawnymi danymi + zapamiętanie danych
    def test_happy_path_login(self):
        login_page = Login(self.driver)
        login_page.login_happy_path()

        list_of_assert_elements = login_page.left_menu_text()
        assert list_of_assert_elements == ["Bookings", "My Profile", "Wishlist", "Newsletter"]

    # testujemy funkcje przywracania zapomnianego hasła
    def test_forget_password_function(self):
        login_page = Login(self.driver)
        login_page.login_forget_password()
        assert 'New Password sent to s.r@wp.pl, Kindly check email' in self.login_page.reset_password_text()

    # testujemy funkcje przywracania zapomnianego hasła, podając błedny email
    def test_forget_password_function_with_wrong_mail(self):
        login_page = Login(self.driver)
        login_page.login_reset_password_wrong_mail()
        assert 'Email Not Found' in self.login_page.reset_password_wrong_mail_text()

    # testujemy funkcje logowania bez podanego emaila
    def test_empty_email_input(self):
        login_page = Login(self.driver)
        login_page.login_empty_email()
        assert 'Invalid Email or Password' in self.login_page.empty_email_text()

    # testujemy funkcje logowania bez podanego hasła
    def test_empty_password_input(self):
        login_page = Login(self.driver)
        login_page.login_empty_password()
        assert 'Invalid Email or Password' in self.login_page.empty_password_text()

    #  testujemy funcje wylogowania
    def test_logout(self):
        login_page = Login(self.driver)
        login_page.logout()
        assert 'LOGIN' in self.login_page.logout_text()

    # testujemy funkcje logowania z błednym adresem email
    def test_wrong_email_input(self):
        login_page = Login(self.driver)
        login_page.login_wrong_email()
        assert 'Invalid Email or Password' in self.login_page.wrong_email_text()
