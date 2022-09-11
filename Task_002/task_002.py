# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import os

# расчет произведений пар чисел, возвращает новый список 
# произведений элнментов исходного списка, формируемого как
# первый * последний, второй * предпоследний, ... 
#   lst - список для расчета
def mult_list_pos(lst:list):
    pos = len(lst) // 2
    if pos*2 < len(lst):
        pos += 1
    
    new_lsf = []
    for i in range(pos):
        new_lsf.append(lst[i] * lst[0-(i+1)]) 

    return new_lsf

## MAIN ##

os.system('cls')

list1 = [2, 3, 4, 5, 6] 
list2 = [2, 3, 5, 6]

print(list1) 
print(mult_list_pos(list1))
print()
print(list2) 
print(mult_list_pos(list2))
