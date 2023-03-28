'''Условие задачи "Большое число":
Даны числа. Нужно определить, какое самое большое число можно из них составить.
'''

'''Формат ввода:
В строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.
'''

'''Формат вывода:
Нужно вывести самое большое число, которое можно составить из данных чисел.
'''

# Пример ввода -> вывода:
inputs = [
    '15 56 2',    # -> 56215
    '1 783 2',   # -> 78321
    '2 4 5 2 10',  # -> 542210
]

# тут ваше решение:
# перевести в инт лист, в цикле: склеить, сунуть в список, отсортировать; последний в списке будет большим
for input in inputs:
    string = input.split(" ")
    sort_string = sorted(string)
    # print(sort_string)
    rev = list(reversed(sort_string))
    print(rev)
    out = ''
    # for i in rev:
    #     k = out + i
    print("".join([out + i for i in rev]))
#
# # for i in range(len(string)):
#     if string[i] >= string[i]:
#         s = s.replace(sim, '')
#
# for i in inputs:
#     out = ''
#     k = list(reversed(sorted(i.split(" "))))
#     print("".join([out + i for i in k]))
