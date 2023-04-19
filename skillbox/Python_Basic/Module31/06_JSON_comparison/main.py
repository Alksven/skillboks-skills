import json


def find_diff(dict1, dict2):
    for key, vel in dict1.items():
        if dict1[key] != dict2[key] and key in diff_list:
            diff[key] = dict1[key]
        if isinstance(dict1[key], dict):
            find_diff(dict1[key], dict2[key])


diff_list = ['company_id', "services", "staff", "datetime"]

diff = dict()

with open('json_new.json', 'r') as json_new, open('json_old.json', 'r') as json_old:
    data1 = json.load(json_new)
    data2 = json.load(json_old)
    find_diff(data1, data2)
print(diff)

with open('result.json', 'w') as result:
    json.dump(diff, result)