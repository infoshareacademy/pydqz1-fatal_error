import name_generator, surname_generator

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


def nickname_random():
    """Funkcja zwracająca nick"""
    nickname = even_letters(name_generator()["Imie"]) + even_letters(surname_generator()["Nazwisko"])
    nickname = {"Nick": nickname}
    return nickname


def email_random():
    """Funkcja zwracająca email"""
    email = nickname_random()["Nick"] + "@wp.pl"
    email = {"Email": email}
    return email
