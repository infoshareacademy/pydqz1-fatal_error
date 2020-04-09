import json

result = []


def save_result():
    with open('Data-Generator/result.json', 'w', encoding="utf-8") as result_file:
        json.dump([result], result_file, ensure_ascii=False)



