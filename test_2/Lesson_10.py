d = {} # словарь
c = {'test' : 1, 'test_2' : "Tesst"}
v = dict (game = 'dict', game_2 = 'dictionary')
b = dict ([(23, 34),(56,87)])
u = dict.fromkeys(['a', 'b', 'c'], 1)
s = {a : a ** 2 for a in range(7)}
v['game'] = 234
print(c['test'])
print(v)
print(b)
print(u)
print(s)

person = {'name' : {'last_name': 'Иванов', 'first_name': 'Иван', 'middle_name': 'Иванович'},
          'address': ['г. Андрюшки', 'ул. Васильковская д. 23б', 'кв.12'],
          'phone': {'home_phone': '34-67-12', 'mobile_phone': '8-564-345-23-65', 'mobile_phone_2': 'Нет'}}
print(person['name']['last_name'])
print(person['address'][1])

print(person.keys()) # возвращает ключи
print(person.values()) # возвращает все значения в словаре
person.clear() # очищает словарь
print(person)