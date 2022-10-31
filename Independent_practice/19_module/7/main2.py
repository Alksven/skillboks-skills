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
            "name": "Bfob",
            "age": 8
        }
    ]
}

childrens_dict = {}
for child in family_member["children"]:
    childrens_dict[child["name"]] = child["age"]

search_bob = childrens_dict.get("Bob", None)
if search_bob:
    print("Bob найден")
else:
    print("Bob-а нету!")

childrens_surname = family_member.get("surname", None)
if childrens_surname:
    print(childrens_surname)
else:
    print("Nosurname")