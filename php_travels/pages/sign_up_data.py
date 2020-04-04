import random

from helpers.name_generator import name_generator
from helpers.password_generator import password_generator
from helpers.surname_generator import surname_generator
from helpers.email_generator import email_generator


class SignUpData:
    def __init__(self):
        self.first_name_input = name_generator()
        self.last_name_input = surname_generator()
        self.mobile_number_input = random.randint(100000000, 999999999)
        self.email_input = email_generator()
        self.password_input = password_generator()
        self.confirm_password_input = self.password_input
