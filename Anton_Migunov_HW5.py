import string
import random
import zipfile

PASSWORD_LENGTH = 4


def extract_archive(file_to_open, password):
    """
    Функция открывает архив с паролем и возвращает результат операции (bool)
    """
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False


def build_pass():
    empty = ''
    for _ in range(PASSWORD_LENGTH):
        empty += random.choice(string.digits)
    return empty


def hack_archive(file_name):
    """
    Функция брутфорсит запароленный архив
    """
    file_to_open = zipfile.ZipFile(file_name)  # объект архива
    wrong_passwords = []  # список паролей, которые не подошли
    tries = 0  # колличество неудачных попыток

    while True:
        """
        Здесь необходимо реализовать: 
            1. Случайную генерацию пароля, который будет соответствовать условиям:
                * длина - 4 символа (`PASSWORD_LENGTH`)
                * допустимые символы пароля - только цифры
                * type(password) == str
            2. Открытие архива со сгенерированым паролем - `extract_archive(file_to_open, password)`
            При удачном открытии (True) - прервать цикл
            При неудачи (False) - добавить пароль в список `wrong_passwords` и больше не проверять данный пароль
            3. Счетчий неудачных попыток
        """
        password = build_pass()
        if password not in wrong_passwords:
            if extract_archive(file_to_open, password):
                break
            else:
                tries += 1
                wrong_passwords.append(password)

    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')


#############
filename = 'misc/task.zip'
hack_archive(filename)
