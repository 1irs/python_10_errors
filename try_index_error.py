list1 = ['a', 'b', 'c']
index = 0
#while True:
try:
    index = int(input('Какой элемент напечатать?'))
    print(list1[index])
    #break
except IndexError:
    #print(f'Увы, элемента под индексом {index} в списке list1 нет. У нас всего {len(list1)} элементов.')
    print('Такого индекса нет, поэтому вернем просто Щ')
