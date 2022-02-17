def f1():
    print(2/0)


def f2():
    f1()


def f3():
    f2()


f3()
