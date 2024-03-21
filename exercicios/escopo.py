pi = 3.14159


def func1():
    num = 10
    print("func1")
    print(pi)
    print(num)
    num = num + 1
    return num


num = func1()
print(num)