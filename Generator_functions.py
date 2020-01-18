import random
import generator_adresu
from generator_adresu import ver2
from name_plus_surname_generators import surname_generator, name_generator
import json


# funkcje edycji napisu
def even_letters(before_even):
    new_string_list = []
    a = 2
    for letters in before_even:
        if a % 2 == 0:
            new_string_list.append(letters)
        a += 1
    new_string_str = "".join(new_string_list)
    return new_string_str


# Funkcja zwracająca adres
def address_random(save_to_file=False):
    address = ver2.print_address()
    if save_to_file == True:
        save_result(address)
    return address


# Funkcja zwracająca imię
def name_random(save_to_file=False):
    name = name_generator.name_generator()
    name = {"Imie":name}
    if save_to_file == True:
        save_result(name)
    return name


# Funkcja zwracająca nazwisko
def surname_random(save_to_file=False):
    surname = surname_generator.surname_generator()
    surname = {"Nazwisko":surname}
    if save_to_file == True:
        save_result(surname)
    return surname


# Funkcja zwracająca
def nickname_random(save_to_file=False):
    nickname = even_letters(name_random()["Imie"]) + even_letters(surname_random()["Nazwisko"])
    nickname = {"Nick":nickname}
    if save_to_file == True:
        save_result(nickname)
    return nickname

# Funkcja zwracajaca email
def email_random(save_to_file=False):
    email = nickname_random()["Nick"] + "@wp.pl"
    email = {"Email":email}
    if save_to_file == True:
        save_result(email)
    return email


# Tworzenie pełnego pakietu danych w postaci osoby
def create_person(save_to_file=False):
    name = name_random()
    surname = surname_random()
    nickname = even_letters(name["Imie"]) + even_letters(surname["Nazwisko"])
    email = nickname + "@wp.pl"
    address = address_random()
    person = {
        "Imie": name["Imie"],
        "Nazwisko": surname["Nazwisko"],
        "Nick": nickname,
        "Email": email,
        "Adres": "Miasto: {} Ulica: {} Numer: {}".format(address["Adres"],address["Street"],address["Number"])
    }
    if save_to_file == True:
        save_result(person)
    return person


def save_result(result):
    with open('result.json', 'w') as result_file:
        json.dump([result], result_file)
