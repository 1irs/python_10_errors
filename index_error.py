list1 = ['a', 'b', 'b', 'd', 'e']

print(len(list1))
for index in range(len(list1)+1):
    # Индекса 5 нет в list1, потому что последний индекс 4.
    print(f"Текущий индекс: {index}")
    print(list1[index])
    if list1[index] == list1[index+1]:
        print('Два подряд равны')


my_dict = {
    'last_name': 'Obrizan'
}

#my_dict['first_name'] = 'Vladimir'
print(my_dict.get('first_name', 'РЕСПОНДЕНТ ПОЖЕЛАЛ ОСТАТЬСЯ НЕИЗВЕСТНЫМ'), my_dict['last_name'])

