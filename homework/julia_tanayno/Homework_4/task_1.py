my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['one', 'two', 'three', 'four', 'five'],
    'dict': {
        'Germany': 'Berlin',
        'Austria': 'Viena',
        'Netherlands': 'Amsterdam',
        'Belgium': 'Brussel',
        'France': 'Paris'
    },
    'set': {2.21, 3.14, 9.8, 14.2, 7.7}
}

# выводим на экран последний элемент кортежа tuple
print(my_dict['tuple'][-1])

# добавляем элемент в конец списка list, удаляем второй элемент
my_dict['list'].append('six')
my_dict['list'].pop(1)

# добавляем элемент в словарь dict с ключом ('i am a tuple')
my_dict['dict'][('i am a tuple',)] = 'hello'
# удаляем элемент
my_dict['dict'].pop('Austria')

# добавляем новый элемент в set, удаляем элемент
my_dict['set'].add(66)
my_dict['set'].remove(3.14)

print(my_dict)
