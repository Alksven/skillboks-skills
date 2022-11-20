server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for i in server_data:
    print(f'{i}:')
    for i_2, i_3 in server_data[i].items():
        print(f'    {i_2}: {i_3}')