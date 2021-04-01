l = []
list = [2,5,'x', 34, 3.4, ['s','t']]
print(list)
a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print(a)
l.append(23)
l.append(37)
l.append(37)
l.append(37)
b = [68,90]
l.extend(b)
l.insert(1, 100)
l.remove(37)
l.pop(0)
print(l.index(90))
print(l.count(37))
print(l)
l.sort()
print(l)
l.reverse()
print(l)
l.clear()
print(l)