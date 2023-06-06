
# def main_function():
#     print('Я внутри функции!')
#
# main_function()
#
# def main_function1(a):
#     print(f'Я печатаю переменную {a}!')
#
# main_function1(5)
#
#
# a = 78
# def main_function2():
#     print(f'Я печатаю переменную {a}!')
#
# main_function2()
# main_function1(5)

# def main_function3(a, b, c):
#     return f'Я печатаю переменную {a} {b}'
#
# print((main_function3(6,'a',8)))
#
# def summ_digits(a,b):
#     c = a+b
#     return c
# print(summ_digits(2,6))
#
# def summ_digits1(a,b):
#     c = a+b
#
# print(summ_digits1(2,6))


# def create_list():
#     my_list =[]
#     for i in range(10):
#         my_list.append(i)
#     return my_list
#
# print(create_list())
#
# def create_list_size(size):
#     my_list = []
#     for i in range(size):
#         my_list.append(i)
#     return my_list
#
# print(create_list_size(5))
# print(create_list_size(15))

# def change_num(num: int, name: str) -> str:
#     num *= 10
#     num //= 5
#     return f'Новое число {name} - {num}'
#
# print(change_num(10, "большое"))
#
# def change_num1(num: int, name: str = "ПО УМОЛЧАНИЮ") -> str:
#     num *= 10
#     num //= 5
#     return f'Новое число {name} - {num}'
#
# print(change_num1(10, "большое"))
# print(change_num1(10))

# def change_num2(num: int, *args, **kwargs) -> int:
#     num *= 10
#     for item in args:
#         if isinstance(item, int):
#             num *= item
#     return num
#
#
# print(change_num2(10, 10))
# print(change_num2(10))
# print(change_num2(10, 10, 5, 'kljlkj', 2, 'jhlkj'))

def change_num3(num: int, *args, **kwargs) -> int:
    num *= 10
    for item in args:
        if isinstance(item, int):
            num *= item
    print(args)
    print(kwargs)
    return num

print(change_num3(10, 10, 5, 'kljlkj', 2, name='jhlkj', age=90))