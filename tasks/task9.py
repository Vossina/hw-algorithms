'''Условие задачи "Cкобочная последовательность":
Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:

- пустая строка - правильная скобочная последовательность;
- правильная скобочная последовательность, взятая в скобки одного типа, – правильная скобочная последовательность;
- правильная скобочная последовательность с приписанной слева или справа правильной скобочной последовательностью — тоже правильная.
На вход подаётся последовательность из скобок трёх видов: [], (), {}.

Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную последовательность и возвращает True,
если последовательность правильная, а иначе False.
'''

'''Формат ввода:
На вход подаётся одна строка, содержащая скобочную последовательность. Скобки записаны подряд, без пробелов.
'''

'''Формат вывода:
Выведите «True» или «False».
'''

# Пример ввода -> вывода:
inputs = [
    '[{()}]',    # -> True
    '()',   # -> True
    '()[])',  # -> False
    '',  # -> True
    '[]{)'  # -> False
]


# Используйте написанный класс Stack:
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        if self.items:
            return 'Not Empty'
        return 'Empty'


# тут ваше решение:
def is_correct_bracket_seq(bracket_seq):
    bracket_open = ['[', '(', '{']
    bracket_close = [']', ')', '}']

    if not bracket_seq:
        return True
    if bracket_seq[0] in bracket_close:
        return False

    for i in bracket_seq:
        if i in bracket_open:
            stack.push(i)
        elif i == ')' and stack.isEmpty() == 'Not Empty' \
                and stack.peek() == '(':
            stack.pop()
        elif i == ']' and stack.isEmpty() == 'Not Empty' \
                and stack.peek() == '[':
            stack.pop()
        elif i == '}' and stack.isEmpty() == 'Not Empty' \
                and stack.peek() == '{':
            stack.pop()
        else:
            return False

    if stack.isEmpty() == 'Not Empty':
        return False
    return True
    # for i in bracket_seq:
    #     if i in bracket_open:
    #         stack.push(i)
    #     elif i in bracket_close:
    #          if len(stack) == 0:
    #             return False
    #         index = bracket_close.index(i)
    #         open_bracket = bracket_open[index]
    #         if stack[-1] == open_bracket:
    #             stack = stack[:-1]
    #         else:
    #             return False
    # return (not stack)

    # if bracket_seq.isEmpty() or bracket_seq.peek() == bracket_seq[0]:  это мое
    #     print('да')
    # else:
    #     print(False)


stack = Stack()
for input in inputs:
    bracket_seq_list = list(input)
    print(is_correct_bracket_seq(bracket_seq_list))
