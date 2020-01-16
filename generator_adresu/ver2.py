
import random
from random import randint


def open_file_1():
    file_1 = open('/home/marek/Desktop/generator/cities_list')
    open_file_1 = file_1.read()
    for i in open_file_1:
        if ',' in i:
            cities = open_file_1.replace(",", "")
    cities = cities.split()

    return cities

def open_file_2():
    file_2 = open('/home/marek/Desktop/generator/streets_list')
    open_file_2 = file_2.read()
    for i in open_file_2:
        if ',' in i:
            streets = open_file_2.replace(",", "")
    streets = streets.split()

    return streets

def complete_address(cities,streets):
    numbers = []
    complete_address = []
    city = random.choice(cities)
    street = random.choice(streets)
    numbers.append(randint(0, 1000))
    addres = city, street, str(numbers[0])
    complete_address.append(addres)

    full_address = {'Adres' : city,
                    'Street' : street,
                    'Number' : numbers[0]}


    return  full_address

def print_address():
    dane = complete_address(get_city,get_street)
    print(dane)


get_city = open_file_1()
get_street = open_file_2()
complete_address(get_city,get_street)
print_address()

