from generator_adresu import ver2
from name_plus_surname_generators import surname_generator, name_generator
import json


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


def address_random(save_to_file=False):
    """funkcja zwracająca adres"""
    address = ver2.print_address()
    if save_to_file:
        save_result(address)
    return address


def name_random(save_to_file=False):
    """Funkcja zwracająca imię"""
    name = name_generator.name_generator()
    name = {"Imie": name}
    if save_to_file:
        save_result(name)
    return name


def surname_random(save_to_file=False):
    """Funkcja zwracająca nazwisko"""
    surname = surname_generator.surname_generator()
    surname = {"Nazwisko": surname}
    if save_to_file:
        save_result(surname)
    return surname


def nickname_random(save_to_file=False):
    """Funkcja zwracająca nick"""
    nickname = even_letters(name_random()["Imie"]) + even_letters(surname_random()["Nazwisko"])
    nickname = {"Nick": nickname}
    if save_to_file:
        save_result(nickname)
    return nickname


def email_random(save_to_file=False):
    """Funkcja zwracająca email"""
    email = nickname_random()["Nick"] + "@wp.pl"
    email = {"Email": email}
    if save_to_file:
        save_result(email)
    return email


def create_person(save_to_file=False):
    """Funkcja torząca pełen pakiet danych osoby"""
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
        "Adres": "Miasto: {} Ulica: {} Numer: {}".format(address["Adres"], address["Street"], address["Number"])
    }
    if save_to_file:
        save_result(person)
    return person

# Zapis danych do pliku w formacie .json
def save_result(result):
    """Funkcja do zapisu rezultatu"""
    with open('Data-Generator/result.json', 'w', encoding="utf-8") as result_file:
        json.dump([result], result_file, ensure_ascii=False)
