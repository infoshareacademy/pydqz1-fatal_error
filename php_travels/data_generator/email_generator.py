from data_generator.name_generator import name_generator
from data_generator.surname_generator import surname_generator
import random

def even_letters(before_even):
    """Funkcja do edycji napisu"""
    new_string_list = []
    a = 2
    for letters in before_even:
        if a % 2 == 0:
            new_string_list.append(letters)
        a += 1
    new_string_str = "".join(new_string_list)
    return new_string_str

def nickname_generator():
    """Funkcja zwracająca nick"""
    nickname = even_letters(name_generator()["name"]) + even_letters(surname_generator()["surname"])
    nickname = {"nick": nickname}
    return nickname

def email_generator():
    """Funkcja zwracająca email"""
    email = nickname_generator()["nick"] + str(random.randint(15, 1000)) + "@wp.pl"
    email = {"email": email}
    return email
