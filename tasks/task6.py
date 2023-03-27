'''Условие задачи "Степень четырёх":
Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.
Подсказка: степенью четвёрки будут все числа вида 4^n (4 возводится в степень n), где n – целое неотрицательное число.
Например, 4^1 = 4, значит, 4 - степень четверки.
Например, 4^2 = 16, значит, 16 - степень четверки.
Например, 4^3 = 64, значит, 64 - степень четверки.
'''

'''Формат ввода:
На вход подаётся целое число в диапазоне от 1 до 10000.
'''

'''Формат вывода:
Выведите «True», если число является степенью четырёх, «False» –— в обратном случае.
'''

# Пример ввода -> вывода:
inputs = [
    '15',   # -> False
    '16',   # -> True
    '4',    # -> True
    '123',  # -> False
    '256'   # -> True
]

# тут ваше решение:
for input in inputs:
    if int(input) % 4 == 0:
        print(True)
    else:
        print(False)
