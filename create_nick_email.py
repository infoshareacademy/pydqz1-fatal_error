import random
import generator_adresu
from generator_adresu import ver2
from name_plus_surname_generators import surname_generator, name_generator
# listy danych do generatora
# names = ['Jacek', 'Wacek', 'Bogdan', 'Alina', 'Halina', 'Malina']
# surnames = ['Kocur', 'Strzyż', 'Zwyż', 'Boruta', 'Blacha', 'Krach']
# persons_list = []


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


def email_random():
    email = nickname_random()["Nick"] + "@wp.pl"
    return {"Email":email}
# ["Imie"]
# ["Nazwisko"]
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


def add_person_to_list():
    global persons_list
    created_person = create_person()
    persons_list.append(created_person)
    print("Created person:\n", created_person)


# dane_jakies = ver2.print_address()
# print(name_random())
# print(surname_random())
# print(dane_jakies)
# {'Adres': 'Zielona', 'Street': 'Ciemna', 'Number': 604}