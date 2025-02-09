'''Условие задачи "Палиндром":
Помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.
'''

'''Формат ввода:
В единственной строке записана фраза или слово. Буквы могут быть только латинские.
Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.
'''

'''Формат вывода:
Выведите «True», если фраза является палиндромом, и «False», если не является.
'''

# Пример ввода -> вывода:
inputs = [
    'A man, a plan, a canal: Panama',  # -> True
    'zo',                              # -> False
    '10001',                           # -> True
    '123'                              # -> False
]

# тут ваше решение:
for strings in inputs:
    new_string = []
    for char in strings:
        if char.isalnum():                  # проверка является ли символ буквенно-цифровым
            new_string.append(char.lower())  # добавление всех символов в список new_string
    new_string = "".join(new_string)          # склеивание символов
    if new_string == new_string[::-1]:         # проверка на палиндром
        print(True)
    else:
        print(False)
