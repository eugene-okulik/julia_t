PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list1 = PRICE_LIST.split('\n')
new_dict = {
    name: int(price[:-1]) for item in list1 for name, price in [item.split()]
}

print(new_dict)
