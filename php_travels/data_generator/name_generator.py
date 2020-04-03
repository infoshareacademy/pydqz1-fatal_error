import json
import random


def read_names():
    with open("names.json", "r", encoding="utf-8") as name_file:
        json_file = name_file.read()
        names = json.loads(json_file)  #ensure_ascii=False
        return names

def name_generator():
    names = read_names()
    name = random.choice(names)
    return name
