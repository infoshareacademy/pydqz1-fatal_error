import random
import generator_adresu
from generator_adresu import ver2
from name_plus_surname_generators import surname_generator, name_generator


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
def address_random():
    address = ver2.print_address()
    return address


# Funkcja zwracająca imię
def name_random():
    name = name_generator.name_generator()
    return {"Imie":name}


# Funkcja zwracająca nazwisko
def surname_random():
    surname = surname_generator.surname_generator()
    return {"Nazwisko":surname}


# Funkcja zwracająca
def nickname_random():
    nickname = even_letters(name_random()["Imie"]) + even_letters(surname_random()["Nazwisko"])
    return {"Nick":nickname}

# Funkcja zwracajaca email
def email_random():
    email = nickname_random()["Nick"] + "@wp.pl"
    return {"Email":email}


# Tworzenie pełnego pakietu danych w postaci osoby
def create_person():
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
    return person