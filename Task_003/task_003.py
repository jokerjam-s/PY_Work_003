# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#
import os

# список для обработки
list = [1.1, 1.2, 3.1, 5, 10.01]


os.system('cls')
print(list)

for i in range(0, len(list)):
    list[i] = round(list[i] % 1, 2)

val = max(list) - min(list)

print(list)
print(val)