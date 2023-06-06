number = 1
print(bool(number))

if 1:
    print('Зашли в тело IF 1')

if 2351:
    print('Зашли в тело IF 2')

if 0:
    print('Зашли в тело IF 3')

number = '7'

if number.isdigit() and 0 < int(number) < 10:
    print('Зашли в тело IF 4')

lenght = 4
width = 3
count = 24

if lenght * width > count and count % lenght == 0 or count % width == 0: # некорретно, так как получаестя от шоколадки размером 12 кусков отломили 24 куска. Это из за того что and работает как сложение
    print('Ура! Все получилось')
if lenght * width > count and (count % lenght == 0 or count % width == 0):
    print('Ура! Все получилось')

# while True:
#     number = input('Введите число: ')
#     if number.isdigit():
#         pass
#     print('Это число')

# while True:
#     number = input('Введите число: ')
#     if number.isdigit():
#         continue
#     print('Это не число')

for i in 'проверка':
    if i == 'э':
        print('э есть')
        break
else:
    print('э нет')

trigger = True
count = 0
for i in 'проверка кк':
    if i == 'к':
        count += 1
        print(f'к есть уже {count} раз')
        trigger = False
if trigger:
    print('э нет')



for i in 'abc':
    for k in range(4):
        for m in ['!', '?']:
            print(i,k,m)


some_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in some_list:
    match('zero' if not number else number % 2):
        case 0:
            print('even')
        case 1:
            print('odd')
        case 'zero':
            print('zero')
        case _:
            print('det lost')