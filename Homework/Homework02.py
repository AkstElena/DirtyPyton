

'''
1. Игра Fizz-Buzz
Есть детская игра FizzBuzz, где нужно называть числа подряд, соблюдая всего три правила:
Если число делится на 3, вместо него надо сказать «Fizz».
Если число делится на 5, вместо него надо сказать «Buzz».
А если число делится одновременно на 3 и на 5, то надо вместо него сказать «FizzBuzz».
На вход подается число num, нужно вывести числа или слова по порядку от 1 до num (включительно) согласно правилам игры
'''
# number = int(input('Введите целое положительное число больше единицы: '))
# if number > 1:
#     result_list = []
#     for i in range(1, number+1):
#         if i % 3 == 0 and i % 5 != 0:
#             result_list.append('Fizz')
#         elif i % 5 == 0 and i % 3 != 0:
#             result_list.append('Buzz')
#         elif i % 5 == 0 and i % 3 == 0:
#             result_list.append('FizzBuzz')
#         else:
#             result_list.append(i)
#     print(*result_list)
# else:
#     print('Необходимо ввести число больше единицы!')

'''
2. Какого цвета клетка
На вход подается обозначение шахматной клетки, необходимо вывести ее цвет
'''
# chess_cage = input('Введите обозначение клетки: ')
# if ' ' in chess_cage:
#     chess_cage = chess_cage.split()
# else:
#     chess_cage = [chess_cage[0], chess_cage[-1]]
#
# chess_board = [{'Белая клетка': [{0: ['a', 'c', 'e', 'g']}, {1: ['b', 'd', 'f', 'h']}]},
#                {'Черная клетка': [{1: ['a', 'c', 'e', 'g']}, {0: ['b', 'd', 'f', 'h']}]}]
# i = 0
# for i in range(len(chess_board)):
#     for k, v in chess_board[i].items():
#         j = 0
#         for j in v:
#             for key, value in j.items():
#                 m = 0
#                 for m in range(len(value)):
#                     if value[m] == chess_cage[0] and int(chess_cage[1]) % 2 == key:
#                         print(k)


'''
3. Дан список чисел. Создать новый список, который будет содержать только уникальные элементы исходного списка
'''
# from random import randint
# my_list = [int(randint(0, 10)) for i in range(0, 20)]
# print(my_list)
# my_list_new = list(set(my_list))
# print(my_list_new)

'''
4. Принимаем с консоли число и выводим две последовательности Фибоначчи и Негафибоначчи (можно прочитать в wiki что это)
Пример: Вводим 8
[-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
# def fib(number):
#     if number in [1, 2]:
#         return 1
#     else:
#         return fib(number-1) + fib(number-2)
#
# def nega_fib(number):
#     if number == -1:
#         return 1
#     elif number == -2:
#         return -1
#     else:
#         return nega_fib(number+2) - nega_fib(number+1)
#
# number = int(input('Введите число знаков последовательности Фибоначчи: '))
# fib_list = []
# for i in range(-number, 0):
#     fib_list.append(nega_fib(i))
# fib_list.append(0)
# for i in range(1, number+1):
#     fib_list.append(fib(i))
# print(fib_list)