
def create_website(product, struct, title='title', h2='h2'):
    if title in struct:
        struct[title] = 'Куплю/продам {} недорого'.format(product)
    if h2 in struct:
        struct[title] = 'У нас самая низкая цена на {}'.format(product)
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = create_website(product, sub_struct, title='title', h2='h2')
            if result:
                break
    else:
        result = None

    return result


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам iPhone недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

num_of_website = int(input('Сколько сайтов:'))

for i in range(num_of_website):
    name_product = input('Введите название продукта для нового сайта: ')
    print('Сайт для', name_product)
    create_website(name_product, site)





