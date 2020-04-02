import random

from data_generator.email_generator import nickname_generator
from data_generator.surname_generator import surname_generator


def password_generator():
    """Funkcja zwracająca email"""
    password = nickname_generator()["nick"] + str(random.randint(15, 1000)) + surname_generator()["surname"]
    password = {"password": password}
    return password