import json
import random

result = []

def read_names():
    """Funkcja odczytująca/dekodująca imiona z pliku"""
    with open("names.json", "r", encoding="utf-8") as name_file:
        json_file = name_file.read()
        names = json.loads(json_file)  #ensure_ascii=False
        return names

def name_generator():
    """Funkcja zwracająca randomowe imię"""
    names = read_names()
    name = random.choice(names)
    return name

def read_surnames():
    """Funkcja odczytująca/dekodująca nazwiska z pliku"""
    with open("surnames.json", "r", encoding="utf-8") as surname_file:
        json_file = surname_file.read()
        surnames = json.loads(json_file)  #ensure_ascii=False
        return surnames

def surname_generator():
    """Funkcja zwracająca randomowe nazwisko"""
    surnames = read_surnames()
    surname = random.choice(surnames)
    return surname

def phone_number_generator():
    """Funkcja zwracająca dziewięcio cyfrowy numer"""
    phone_number = random.randint(100000000, 999999999)
    return phone_number

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

def password_generator():
    """Funkcja zwracająca hasło"""
    password = nickname_generator()["nick"] + str(random.randint(15, 1000)) + surname_generator()["surname"]
    password = {"password": password}
    return password

def save_result():
    """Funkcja do zapisu danych w pliku result.json"""
    with open('result.json', 'w') as result_file:
        json.dump(result, result_file)

