import json
import random


def read_names():
    with open("data_generator/names.json", "r", encoding="utf-8") as name_file:
        json_file = name_file.read()
        names = json.loads(json_file,  ensure_ascii=False)
        return names


def name_generator():
    names = read_names()
    result = random.choice(names)
    return result