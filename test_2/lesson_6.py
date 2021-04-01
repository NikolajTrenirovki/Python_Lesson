i = 0
while i < 10:
    print(i)
    i += 1
for j in 'hello world':
    if j == 'w':
        continue
    if j == 'r':
        break
    print(j * 2, end ='')
else: print("Буквы r нету в слове")