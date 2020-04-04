import pytest


@pytest.mark.usefixtures('setup_ch', 'setup_ff')
class TestPageFeature:

    # testujemy proces logowania z poprawnymi danymi + zapamiętanie danych
    def test_happy_path_login(self):
        email_data = 'sr@wp.pl'
        password_data = '123456789'
        left_menu_section_tab_list = ["Bookings", "My Profile", "Wishlist", "Newsletter"]
        self.login_page.login_happy_path(email_data, password_data)

        list_of_assert_elements = self.login_page.left_menu_text()
        assert list_of_assert_elements == left_menu_section_tab_list

    # testujemy funkcje przywracania zapomnianego hasła
    def test_forget_password_function(self):
        used_email_data = 's.r@wp.pl'
        self.login_page.login_forget_password(used_email_data)

        assert 'New Password sent to s.r@wp.pl, Kindly check email' in self.login_page.reset_password_text()

    # testujemy funkcje przywracania zapomnianego hasła, podając błedny email
    def test_forget_password_function_with_wrong_mail(self):
        wrong_mail_data = 'srwp.pl'
        self.login_page.login_reset_password_wrong_mail(wrong_mail_data)

        assert 'Email Not Found' in self.login_page.reset_password_wrong_mail_text()

    # testujemy funkcje logowania bez podanego emaila
    def test_empty_email_input(self):
        password_data = '123456789'
        self.login_page.login_empty_email(password_data)

        assert 'Invalid Email or Password' in self.login_page.empty_email_text()

    # testujemy funkcje logowania bez podanego hasła
    def test_empty_password_input(self):
        used_email_data = 's.r@wp.pl'
        self.login_page.login_empty_password(used_email_data)

        assert 'Invalid Email or Password' in self.login_page.empty_password_text()

    #  testujemy funcje wylogowania
    def test_logout(self):
        email_data = 'sr@wp.pl'
        password_data = '123456789'
        self.login_page.logout(email_data, password_data)

        assert 'LOGIN' in self.login_page.logout_text()

    # testujemy funkcje logowania z błednym adresem email
    def test_wrong_email_input(self):
        wrong_email_data = 'srwp.pl'
        password_data = '123456789'
        self.login_page.login_wrong_email(wrong_email_data, password_data)

        assert 'Invalid Email or Password' in self.login_page.wrong_email_text()
