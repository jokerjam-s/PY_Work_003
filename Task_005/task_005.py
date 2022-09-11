# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
# 
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
#

import os

# получить число с консоли
#   message - сообщение для пользователя
def get_int(message: str) -> int:
    return int(input(message))


# расчет ряда чиел фибоначи
#   num - число, для которого идет вычисление
#   direction - направление >=0 положительый ряд, иначе - негативный ряд
def calc_fib(num: int, direction: int = 0):
    fib = [0, 1]
    for n in range(1, num):
        fib.append(fib[-1] + fib[-2])
    
    if direction < 0:
        for i in range(2, len(fib), 2):
            fib[i] *= -1
        
    return fib


## MAIN ##
os.system('cls')

num = get_int('Введите число: ')

twice_fib = calc_fib(num, -1)
twice_fib.remove(0)
twice_fib.reverse()
twice_fib.extend(calc_fib(num))

print(twice_fib)

