def value_search(key, struct, time=-1):
    if time == 0:
        return None
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = value_search(key, sub_struct, time - 1)
            if result:
                break
    else:
        result = None

    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key_find = input('Введите искомый ключ:')
want_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()

if want_depth == 'y':
    depth = int(input('Введите максимальную глубину: '))
    value = value_search(key_find, site, depth)
    print('Значение ключа:', value)

elif want_depth == 'n':
    value = value_search(key_find, site)
    print('Значение ключа:', value)

