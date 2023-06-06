# my_list = [1, '2', True,  [4, 5], {'key': 35}]
# print(my_list[4])
#
# a = 5
# b = a
# a = a + 1
# print(a, b)
#
# a = [1, 2, 3]
# b = a
# a.append(4)
# b.append(5)
# print(a, b)
#
# a = [1, 2, 3]
# b = a.copy()
# a.append(4)
# b.append(5)
# print(a, b)

# a = [1, 2, 3, [1, 2, 3]]
# b = a.copy()
# a[3][1] = 9
# print(a)
# print(b)
#
# from copy import deepcopy
# a = [1, 2, 3, [1, 2, 3]]
# b =deepcopy(a)
# a[3][1] = 9
# print(a)
# print(b)

# my_list = [1, 2, 3, 2, 1]
#
# my_string = '123'
# my_string = list(my_string)
#
# print(my_list)
# print(my_string)
#
# print(my_list[1::2])

# my_list = [1, 2, 3, 2, 1]
# my_list = [str(item) for item in my_list]
# print(my_list)
#
# my_list = ['1', '2', '3', '2', '1']
# print('-'.join((my_list)))
# print(' '.join((my_list)))
# print(''.join((my_list)))

# my_tuple = (1, 2, 3, 'r')
#
# dig1, dig2, dig3, let = my_tuple
# print(dig1)
# print(dig2)
# print(dig3)
# print(let)
#
# my_tuple = (1, 2, 3, 'r')
# print(*my_tuple, sep='-')
# dig1, *dig2 = my_tuple
# print(dig1)
# print(dig2)


# my_set = {1, 2, 3, 4, 5, 6, 6}
# my_set.pop()
# print(my_set)

# my_set = {str(i) for i in range(100)}
# for _ in range(6):
#     print(my_set.pop())
#     input()

my_dict = {'one': 1, 'two': 2, 'три': 3 }
# my_dict1 = {'Key': {1234: {'key': 900}}}
# print(my_dict1.get('Key').get(1234).get('key'))
# print(my_dict.get('one'))
# print(my_dict.get(1))
# my_dict[4] = 'four'
# print(my_dict)
# print(my_dict.get(5, "нет такого ключа"))

# my_dict = {'one': 1, 'two': 2, 'три': 3 }
# new_dict = {'one': 10, 'two': 21, 'четыре': 4}
# my_dict.update(new_dict)
# print(my_dict)

# keys = ("g", 'kdf')
# print(my_dict.fromkeys(keys, ''))

# my_dict = {'one': 1, 'two': 2, 'три': 3}
#
# for i in my_dict:
#     print(i)
#
# for i in my_dict.keys():
#     print(i)
#
# for i in my_dict.values():
#     print(i)
#
# for i in my_dict.items():
#     print(i)

# my_list = []
# for i in range(10):
#     my_list.append(i)
# print(my_list)
#
# my_list = [i for i in range(10)]
# print(my_list)
#
# my_list = [i**3 for i in range(10) if not i%2]
# print(my_list)
#
# my_list = [(i, i**3) for i in range(10) if not i%2]
# print(my_list)

from random import randint
# my_set = {randint(0,10) for i in range(20)}
# print(my_set)
#
# uniq_list = set()
# while len(uniq_list) <= 10:
#     uniq_list.add(randint(0,15))
# print(uniq_list)

my_dict = {i:i**2 for i in  range(20)}
print(my_dict)