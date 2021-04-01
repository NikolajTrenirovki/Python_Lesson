a = {'23', 32}
print(type(a))
print(a)

a = {i ** 2 for i in range(10)}
print(type(a))
print(a)

a = set("Hello")
b = frozenset("Qwerty")
a.add(1)
print(a)
print(len(a))
print(b)
x = 'e'
print(x in a)
t = {23,45,34}
s = {76, 89, 34 ,21}
print(t.isdisjoint(s)) # возвращает true, если множества не имеют общих элементов
print(t == s) # возвращает true, если все элементы множеств равны (порядок не важен)
t.update(s) # добавляет в t все эелементы s
print(t)
r = {12, 23, 78, 34}
t.intersection_update(r) # пересечения
print(t)
r.difference_update(t) # выводит цифры, которые есть в r, но нет в t
print(r)
r.symmetric_difference_update(s) # множества элементов, встречающихся в одном множестве, но не встречающихся в обоих
print(r)
r.add(23)
r.remove(21)
r.discard(12)
r.pop() # удаляет первый элемент из множества
print(r)
r.clear()