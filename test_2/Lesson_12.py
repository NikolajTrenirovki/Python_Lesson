def func(x, a):
    return x + a


print(func(23, 56))


def func_2(x):
    def add(a):
        return x + a

    return add


test = func_2(100)  # x = 100
print(test(200))  # a = 200


def func_3():
    x = 34
    pass


print(func_3())


def func_4(r, t, w=2):
    return w


print(func_4(8, 3))
print(func_4(3, 2, 5))


def func_5(*args):  # аргумнты сохраняются в картеж
    return args


print(2, 3, 5)


def func_6(**args):  # аргументы созраняются в словарь
    return args


print(func_6(a=2, b=3, c=5))
print(func_6(short = 'dict', longer = 'dictionary'))


add = lambda x, y: x + y
print(add(1,5))

print((lambda x, y: x+y)(2, 6))

fun = lambda *args: args

print(fun(2, 56, 7, 'w', ' wer', 7.56))