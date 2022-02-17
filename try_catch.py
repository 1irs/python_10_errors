while True:
    try:
        x = int(input("Введите число: "))
        break
    except ValueError:
        print(f"Это не число, повторите попытку!")

print(f'Вы ввели {x} — это корректное число')

