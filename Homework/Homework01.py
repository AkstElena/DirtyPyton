""" ДЗ на типы данных
1. На вход подается число с плавающей точкой, выведите первую цифра дробной части
"""

# number = float(input('Введите число с плавающей точкой: '))
# result = str(abs(float(int(number)) - number))
# print(result[2])

'''
2. На вход подается целое число, необходимо поменять местами первую и последняя цифру в числе
'''
# number = input('Введите целое число: ')
# if number[0] == '-':
#     print(number[0]+number[-1]+number[2:-1]+number[1])
# else:
#     print(number[-1]+number[1:-1]+number[0])

'''
3. На вход поступает число: найти сумму цифр числа, в том числе если оно отрицательное или вещественное.
'''
'''Мое слишком длинное решение'''
# number = input('Введите число, в том числе отрицательное или вещественное: ')
# result = 0
# if "-" in number:
#     number = number.replace("-","")
#     if "." in number:
#         number = int(number.replace(".", ""))
#         while number > 0:
#             result = result + number % 10
#             number = number // 10
#         print(result)
#     else:
#         number = int(number)
#         while number > 0:
#             result = result + number % 10
#             number = number // 10
#         print(result)
# elif "." in number:
#     number = int(number.replace(".", ""))
#     while number > 0:
#         result = result + number % 10
#         number = number // 10
#     print(result)
# else:
#     number = int(number)
#     while number > 0:
#         result = result + number % 10
#         number = number // 10
#     print(result)

# '''Эталонное решение'''
# number = input('Введите число: ')
# num_list = [int(item) for item in number if item.isdigit()]
# print(sum(num_list))

'''
4. На вход поступает десятичное число, вывести его в виде двоичного
'''

# number = int(input('Введите десятичное число: '))
# result = ''
# while number > 0:
#     result = str(number % 2) + result
#     number = number // 2
# print(result)


'''
5. Дана строка текста, необходимо сформировать из нее две новых строки из символов которые стоят на четных позициях и на нечетных
'''

# my_text = 'Разделить этот текст на нечетные и четные символы'
# print(my_text)
# print(my_text[::2])
# print(my_text[1::2])

'''
6. Проверка на палиндром:
   а. слова
   б. предложения
'''
# my_text = input('Введите текст для проверки на палиндром: ').upper().replace(" ",'')
# point = int(len(my_text)/2)
# count = 0
# for i in range(point):
#     if my_text[i] == my_text[-i-1]:
#         i += 1
#         count += 1
#     else:
#         print('Введенный текст не является палиндромом')
#         break
# if count == point:
#     print('Введенный текс является палиндромом')

'''Эталонное решение через срезы'''
my_text = input('Введите текст для проверки на палиндром: ').upper().replace(" ",'')
if my_text[::-1] == my_text:
    print('Введенный текс является палиндромом')
else:
    print('Введенный текст не является палиндромом')