from typing import Callable
# def sum_two(a, b):
#     return a+b
#
# print(sum_two(4, 5))
#
# new_func = sum_two
# print(new_func(4,5))
#
# def operation(func: Callable, a, b):
#     return func(a,b)
# print(operation(sum_two, 5, 10))

# first = 'klffjdlkf'
# # second = 'fdklkjed'
# # third = 'fdkadafffeert'
# # print(sorted((first, second, third), key=lambda x: x.count('f')))
# # print(max((first, second, third), key=lambda x: x.count('f')))
# # print(min((first, second, third), key=lambda x: x.count('f')))

'''
lambda
обычно не объявляют, сразу в теле решения
'''
# def operation (func, a, b):
#     return func(a,b)
# print(operation((lambda a,b: a+b), 4, 5))

# def outter (a,b):
#     def inner ():
#         print ("Inside")
#     inner()
#     return a+b
# print(outter(5,5))

# def outter1 (a,b):
#     def inner (b):
#         return b*b
#     return a*0,inner(b)
# print(outter1(5,10))

# string = '1234567890'
# num_list = list(string)
# print(num_list)
# num_list = list(map(int, num_list))
# print(num_list)

# num_list = list(filter(lambda x: int(x)%2==0, num_list))
# print(num_list)

# string = '12345sdfs6789asda0'
# num_list = list(string)
# print(num_list)
# num_list = list(filter(lambda x: x.isdigit(), num_list))
# print(num_list)

# n_list = [i**2 for i in range(10) if i%2 == 0]
# print(n_list)

# n_list = [i for i in 'jldhjhklads']
# print(n_list)
#
# for i in n_list:
#     print(i)
#
# for i in enumerate(n_list, 10):
#     print(i)
# for i, letter in enumerate(n_list):
#     print(i, letter)
'''
вместо range
'''

# for i, letter in enumerate(n_list):
#     if letter == "h":
#         n_list[i] ='HH'
# print(n_list)

a_list = [i for i in 'jldhjhklaj']
b_list = [i for i in '123456789025']
c_list = [i for i in '%^$']
print(a_list)
print(b_list)
print(c_list)

new_list = list(zip(a_list, b_list, c_list))
print(new_list)

from  itertools import  zip_longest
new_list = list(zip_longest(a_list, b_list, c_list, fillvalue=0))
print(new_list)

