"""
1. Валидатор паролей. На занятии делали валидацию емейла, тут
    нужно сделать валидацию пароля по такому же принципу.
    Придумать критерии надежного пароля, описать их в условиях.
"""

# # Надежный пароль содержит цифры, буквы обоих регистров и специальные символы. Длина пароля от 12 до 20 символов.
#
# password = input('Enter your password ')
# special_chars = set('!@#$%^&*()_+-={}[];:?.,<>\'\"\\')
# password_chars = set(password)
# validation = True
#
# # Length check
# if not 12 <= len(password) <= 20:
#     validation = False
#
# #  Symbols check
# for state in [password.isdigit(), password.isalpha(), password.islower(), password.isupper(), password.isspace()]:
#     if state:
#         validation = False
#
# if password_chars.intersection(special_chars) == set():
#     validation = False
#
# if validation:
#     print('Valid')
# else:
#     print('Invalid')

"""
2. Создать список, где все элементы будут кратные 5ти (упражнение на функцию range)
"""

# print(list(range(0, 101, 5)))

"""
3. Нарисовать в консоли ёлочку)
"""
#    *
#   ***
#  *****
# *******
#    *
#   ***

# row_map = [1, 3, 5, 7, 9, 1, 3]
#
# for row in range(0, len(row_map)):
#     center = row_map[row]
#     side = (max(row_map) - center) // 2
#     print(' ' * side + '*' * center + ' ' * side + '\n')

"""
4. Задать число (input или number=Ваше число) и посчитать количество цифр в нем
"""

# try:
#     num = int(input('Enter an integer number '))
#     print(len(str(num)))
# except:
#     print('Not an integer number')

"""
5. Сгенерировать произваольный список и развернуть его
"""

# generated_list = [i for i in range(2, 26, 4)]
# print(generated_list)
#
# print(generated_list[::-1])
#
# generated_list.reverse()
# print(generated_list)
