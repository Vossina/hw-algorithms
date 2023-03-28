'''Условие задачи "Лишняя буква":
Васе очень нравятся задачи про строки, поэтому он придумал свою.
Есть 2 строки s и t, состоящие только из строчных букв.
Строка t получена перемешиванием букв строки s и добавлением 1 буквы в случайную позицию.
Нужно найти добавленную букву.
'''

'''Формат ввода:
На вход подается кортеж, содержащий строки s и t.
'''

'''Формат вывода:
Выведите лишнюю букву.
'''

# Пример ввода -> вывода:
inputs = [
    ('abcd', 'abcde'),   # -> e
    ('go', 'ogg'),       # -> g
    ('xtkpx', 'xkctpx')  # -> c
]


# тут ваше решение:
def find_char(s, t):
    for s, t in zip(s, t):
        if s != t:
            return t


for input in inputs:
    s, t = input
    print(s, t)
    s = list(input[0])
    t = list(input[1])
    s = s.sort()
    t = t.sort()
    find_char(s, t)
# for i in range(len(t)):   #  было мое
#     sim = t[i]
#     if sim in s:
#         s = s.replace(sim, '')
#     else:
#         print(sim)
#         break
# res = [x for x in s + t if x not in s or x not in t]  # создавала пользовательский список, но он все равно не так выводит
# print(res)
