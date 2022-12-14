family_member = {
    "name": "Jane",
    "surname": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "Alice",
            "age": 6
        },
        {
            "name": "Baob",
            "age": 8
        }
    ]
}

childrens_dict = dict()
for child in family_member["children"]:
    childrens_dict[child["name"]] = child["age"]

search_bob = childrens_dict.get('Bob', None)
if search_bob:
    print('Bob found.')
else:
    print('Bob not found.')
    exit()

if search_bob:
    print(family_member['surname'])

