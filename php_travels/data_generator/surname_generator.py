import json
import random


def read_surnames():
    with open("data_generator/surnames.json", "r", encoding="utf-8") as surname_file:
        json_file = surname_file.read()
        surnames = json.loads(json_file, ensure_ascii=False)
        return surnames


def surname_generator():
    surnames = read_surnames()
    result = random.choice(surnames)
    return result