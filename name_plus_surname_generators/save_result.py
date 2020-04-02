import json

result = []


def save_result():
    with open('result.json', 'w') as result_file:
        json.dump(result, result_file)



