import json
# result to rzeczy ktore mają być zapisane
result = []


def save_result():
    with open('result.json', 'w') as result_file:
        json.dump(result, result_file)



