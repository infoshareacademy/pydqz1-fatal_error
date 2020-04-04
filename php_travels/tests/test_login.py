import pytest


@pytest.mark.usefixtures('setup_ff', 'setup_ch')
class TestLogin:

    # testujemy proces logowania z poprawnymi danymi + zapamiętanie danych
    def test_happy_path_login_with_valid_data(self):
        email_data = 'sr@wp.pl'
        password_data = '123456789'
        left_menu_section_tab_list = ["Bookings", "My Profile", "Wishlist", "Newsletter"]
        self.login_page.login(email_data, password_data)

        list_of_assert_elements = self.login_page.left_menu_text()
        assert list_of_assert_elements == left_menu_section_tab_list

    # testujemy funkcje zmiany zapomnianego hasła
    def test_forget_password_function_with_existing_email(self):
        existing_email = 's.r@wp.pl'
        self.login_page.login_forget_password(existing_email)

        assert 'New Password sent to s.r@wp.pl, Kindly check email' in self.login_page.reset_password_text()

    # testujemy funkcje zmiany zapomnianego hasła, podając błedny email
    def test_forget_password_function_with_wrong_email(self):
        wrong_email = 'srwp.pl'
        self.login_page.login_forget_password(wrong_email)

        assert 'Email Not Found' in self.login_page.reset_password_wrong_mail_text()

    # testujemy funkcje logowania bez podanego emaila
    def test_with_empty_email_input(self):
        self.login_page.login(password_data='123456789')

        assert 'Invalid Email or Password' in self.login_page.empty_email_text()

    # testujemy funkcje logowania bez podanego hasła
    def test_with_empty_password_input(self):
        email_data = 's.r@wp.pl'
        self.login_page.login(email_data)

        assert 'Invalid Email or Password' in self.login_page.empty_password_text()

    # testujemy funkcje logowania z błednym adresem email
    def test_with_wrong_email_input(self):
        email_data = 'srwp.pl'
        password_data = '123456789'
        self.login_page.login(email_data, password_data)

        assert 'Invalid Email or Password' in self.login_page.wrong_email_text()

    #  testujemy funcje wylogowania
    def test_logout(self):
        email_data = 'sr@wp.pl'
        password_data = '123456789'
        self.login_page.logout(email_data, password_data)

        assert 'LOGIN' in self.login_page.logout_text()
