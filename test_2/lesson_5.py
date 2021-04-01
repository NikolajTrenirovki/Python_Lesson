if 1:
    print("true\n")
    print("ok")
    print("print")
if 0:
    print("false")
    print("строка")
num = "test"
if num == "test":
    print(num)
elif num == "test_2":
    print(num + " строка")
else:
    print(num + " слово")

name = input()
A = "Yes" if name != "test" else "No"
print(A)