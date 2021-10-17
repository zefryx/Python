
# сортировка перестановками
def perestan(list):
    count = 0
    for i in range(1, len(list)):
        per = list[i]
        j = i - 1
        while (j >= 0 and list[j] < per): # сортировка по возрастанию или убыванию
            list[j + 1] = list[j]
            j -= 1
            count += 1
        list[j + 1] = per
    return f'{list}, количество итераций - {count}'

#a = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(f'Список до сортировки                   - {a}')
print (f'Список после сортировки перестановками - {perestan(a)}')
