import os

o = str(input('Вы готовы зарегистрироваться?: '))
if o == 'нет':
    f = str(input('Вы уже зарегистрированы?: '))

a = str(input('Введите ваш логин: '))
b = input('Введите ваш пароль: ')

print('Ваше логин:', a)
print('Ваш пароль', b)
g = str(input('Все верно?: '))
if g == 'да':
    print('Данные сохранены')
elif g == 'нет':
    w = str(input('Хотите начать с начала?: '))
elif w == 'да':
    quit()
else:
    print('Вы что то ввели не верно')
    quit()

if g == 'да':
    file = open('password.txt', 'w+')
    file.write(str(a))
    file.close()

    file = open('password.txt', 'a+')
    file.write(str(b))
    file.close()