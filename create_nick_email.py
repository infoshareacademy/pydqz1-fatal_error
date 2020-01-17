import random

# listy danych do generatora
names = ['Jacek', 'Wacek', 'Bogdan', 'Alina', 'Halina', 'Malina']
surnames = ['Kocur', 'Strzyż', 'Zwyż', 'Boruta', 'Blacha', 'Krach']
persons_list = []

# funkcje globalne
def even_letters(before_even):
    new_string_list = []
    a = 2
    for letters in before_even:
        if a % 2 == 0:
            new_string_list.append(letters)
        a += 1
    new_string_str = "".join(new_string_list)
    return new_string_str

#Funkcja zwracająca adres
def address_random():
    address = "Jana Pawła II 99c/99"
    return address

#Funkcja zwracająca imię
def name_random():
    name = random.choice(names)
    return name

#Funkcja zwracająca nazwisko
def surname_random():
    surname = random.choice(surnames)
    return surname

#Funkcja zwracająca
def nickname_random():
    nickname = even_letters(name_random()) + even_letters(surname_random())
    return nickname

def email_random():
    email = nickname_random() + "@wp.pl"
    return email


def create_person():
    name = name_random()
    surname = surname_random()
    nickname = even_letters(name) + even_letters(surname)
    email = nickname + "@wp.pl"
    address = address_random()
    person = {
        "Imie": name,
        "Nazwisko": surname,
        "Nick": nickname,
        "Email": email,
        "Adres": address
    }
    return person

def add_person_to_list():
    global persons_list
    created_person = create_person()
    persons_list.append(created_person)
    print("Created person:\n", created_person)