"""
1. Написать любую детерменированную функцию (Детерменированная функция = функция, которая возвращает одно и тоже вне
зависимости от парамеметров)
"""

def return_1():
    return 1

# print(return_1())


"""
2. Написать функцию, которая вернет True если число четное и False если не четное
"""


def integer_conformity_check(num: str):
    return True if (num.isdigit() or (num[0] == '-' and num[1::].isdigit())) else False


def parity_check(num: int):
    return True if num % 2 == 0 else False


def main_2():
    user_num = input('Kindly ask you to enter an integer number: ')
    if integer_conformity_check(user_num):
        print(parity_check(int(user_num)))
    else:
        print('I asked you kindly, dumb!')
        raise ValueError


# main_2()


"""
3. Напишите функция is_prime, которая принимает 1 аргумент (число) и возвращает True, если число простое, иначе False
Простое число - это число, которое делится без остатка только на себя и на 1
"""


def conformity_check(num: str):
    return True if num.isdigit() else False


def is_prime(num: int):
    for divider in range(1, round(num ** 0.5)+1):
        if num % divider == 0 and divider != 1 and divider != num:
            print('Number is composite.')
            return False
    return True


def main_3():
    user_num = input('You should put a positive integer number here: ')
    if conformity_check(user_num):
        print(is_prime(int(user_num)))
    else:
        print('Try not to upset me next time...')
        raise ValueError


# main_3()


"""
4. Напишите функцию, которая принимает 1 аргумент (строка) и выполняет следующие действия на каждую из букв строки:
i - инкремент (+1)
d - дикремент (-1)
s - возведение в квадрат
o - добавить число в результативный список
остальные буквы игнорируются
Исходное число = 0
Результативный список = []
Вернуть результативный список
parse("iiisdoso")  ==>  [8, 64] <- это как пример
"""


def parse(num: int, command_string: str):
    result = []
    for command in command_string:
        if command == 'i':
            num += 1
        elif command == 'd':
            num -= 1
        elif command == 's':
            num = num * num
        elif command == 'o':
            result.append(num)
    return result


# print(parse(0, 'iidodsoiioddo'))


"""
5. Написать функцию, которая из строки делает datetime и возвращает результат, если введенный 
формат даты неверный - возвращать None. Аргументы - срока-дата, формат, 
по которому можно привести строку в datetime
"""
from datetime import date


def string_to_date(date_string: str):
    try:
        return date.fromisoformat(date_string)
    except Exception:
        return None


# print(string_to_date('2020-12-20'))
# print(string_to_date('2020-20-12'))
# print(string_to_date('2rt5-*7-gg'))
