def f1():
    return int(input('Введите А'))


def f2():
    return int(input('Введите Б'))


def f3(a, b):
    return a/b


error = True
tries = 0
while error and tries <= 2:
    try:
        a = f1()
        b = f2()
        c = f3(a, b)
        print(c)
        error = False
    except (ValueError, ZeroDivisionError):
        tries += 1
        if tries == 3:
            print('Увы, вы исчерпали все попытки :(')
        else:
            print('Увы, давайте заново')

